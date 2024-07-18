import os
import unstructured_client
from unstructured_client.models import operations, shared
from unstructured.staging.base import dict_to_elements
from langchain.schema import Document

class DataLoader:
    """
    A Custom Data Loader class taking WHR+24 pdf and encoding it into "Lanchain.schema.Document" using unstructured.io.
    
    Input: World Happiness Report 2024 PDF.
    Returns: "langchain.schema.Document" object.
    """

    def __init__(self):
        self.filename = 'WHR+24_ChatBot/WHR+24.pdf'
        os.environ['UNSTRUCTURED_API_KEY'] = 'YOUR_UNSTRUCTURED_API_KEY'  # YOUR UNSTRUCTURED API KEY REQUIRED
        os.environ['UNSTRUCTURED_API_URL'] = 'YOUR_UNSTRUCTURED_API_URL'  # YOUR UNSTRUCTURED API URL REQUIRED

    def UnStructuredPDFLoader(self) -> Document:
        client = unstructured_client.UnstructuredClient(
                                            api_key_auth=os.environ['UNSTRUCTURED_API_KEY'],
                                            server_url=os.environ['UNSTRUCTURED_API_URL']
        )
        with open(self.filename,'rb') as f:
            data = f.read()
            
        # Keeping "strategy" as AUTO and "chunking-strategy" as BY_TITLE   
        req = operations.PartitionRequest(
        partition_parameters=shared.PartitionParameters(
        files=shared.Files(
            content=data,
            file_name=self.filename),
        strategy=shared.Strategy.AUTO,
        chunking_strategy='by_title',
        languages=['eng']
    ),
)
        res = client.general.partition(request=req)
        res_ele = dict_to_elements(res.elements)

        # Wrapping Up in "langchain.schema.document"
        document = []
        for element in res_ele:
          metadata = element.metadata.to_dict()
          document.append(Document(page_content=element.text,metadata=metadata))
            
        return document

        