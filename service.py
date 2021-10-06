from pywps import Process, ComplexOutput, LiteralInput, Format
import json
import time


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
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def runMyProcess(self, request, response):
        # get inputs from request-object
        givenInput = request.inputs['someVal'][0].data
        
        # sleep a while to simulate processing
        response.update_status('Ongoing...', 0)
        time.sleep(3.0)
        response.update_status('Ongoing...', 30)
        time.sleep(3.0)
        response.update_status('Ongoing...', 60)
        time.sleep(3.0)

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