from pywps import Process, ComplexOutput, LiteralInput, Format
import json


class MyProcess(Process):

    def __init__(self):
        # declare inputs and outputs
        inputs = [
            # important: double check that data_type is one that is supported by PyWPS
            LiteralInput('someVal', 'Some value', data_type='integer')
        ]
        outputs = [
            # important: double check that Format is supported by PyWPS
            ComplexOutput('someOutput', 'Some output',
                supported_formats=[Format('application/geo+json', encoding='UTF-8')],
            )
        ]
        # register inputs, outputs and meta-data
        super().__init__(
            self.runMyProcess,
            identifier='MyProcess',
            title='My process',
            abstract='A very simple process',
            inputs=inputs,
            outputs=outputs
        )

    def runMyProcess(self, request, response):
        # get inputs from request-object
        givenInput = request.inputs['someVal'][0].data
        theOutput = {
            'type': 'FeatureCollection',
            'features': [],
            'properties': {
                'givenInput': givenInput
            }
        }
        # put outputs into response-object
        response.outputs['someOutput'].data = json.dumps(theOutput)
        # return mutated response-object
        return response