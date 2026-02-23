from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import faiss
import numpy as np
import nest_asyncio
from pyngrok import ngrok
import uvicorn

#Allow nested loops 
nest_asyncio.apply()

#Initialize FastAPI
app = FastAPI()

#Initialize models
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
generator = pipeline("text2text-generation",model = "google/flan-t5-base")

#documents
documents = [
    "Azure Machine Learning allows deployment of models in the cloud.",
    "Transformers use attention mechanisms to process sequential data efficiently.",
    "Vector databases enable efficient similarity search using embeddings.",
    "Cloud computing provides scalable AI infrastructure.",
    "Machine learning models can be deployed using REST APIs for real-time inference.",
    "Docker containers help package AI models with their dependencies for consistent deployment.",
    "Kubernetes orchestrates containerized applications at scale.",
    "Model versioning ensures reproducibility and tracking of experiments.",
    "Continuous integration and continuous deployment pipelines automate model updates.",
    "Feature engineering improves the predictive performance of machine learning systems.",
    "Neural networks learn hierarchical representations of data.",
    "Transfer learning allows models to leverage pre-trained knowledge.",
    "Fine-tuning adapts pre-trained models to specific tasks.",
    "Batch inference processes large datasets efficiently.",
    "Real-time inference is used in applications like chatbots and recommendation systems.",
    "Monitoring deployed models helps detect performance degradation.",
    "Model drift occurs when data distribution changes over time.",
    "Data preprocessing includes cleaning, normalization, and encoding.",
    "Hyperparameter tuning optimizes model performance.",
    "Embeddings convert text into numerical vector representations.",
    "Cosine similarity measures semantic similarity between vectors.",
    "L2 distance calculates Euclidean distance between embeddings.",
    "Distributed computing accelerates large-scale AI workloads.",
    "GPU acceleration significantly speeds up deep learning training.",
    "Scalable storage solutions are essential for big data applications."
]

doc_embeddings = embedding_model.encode(documents)
doc_embeddings = np.array(doc_embeddings).astype("float32")

dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(doc_embeddings)

@app.get("/ask")
def ask(question: str):
  query_embedding = embedding_model.encode([question])
  query_embedding = np.array(query_embedding).astype("float32")

  distance, indices = index.search(query_embedding, 2)
  retrieved_docs = [documents[i] for i in indices[0]]
  context = " ".join(retrieved_docs)

  prompt = f"""
  You are an expert AI assistant.
  Using the context below, provide a detailed explanation in full sentences.

  context:
  {context}

  Question:
  {question}

  Answer:
  """

  response = generator(prompt, max_new_tokens=200, do_sample=True, temperature=0.7)

  return{"answer": response[0]['generated_text']}

if __name__ == "__main__":
   ngrok.set_auth_token("39nrON5sXnBO9LoEieiC5mg4xBg_5tDzV1v12v4tcKFwvBHtn")

   public_url = ngrok.connect(8000)
   print(f"\n✅ SUCCESS! Follow these steps:")
   print(f"1. Open this link: {public_url.public_url}/docs")
   print(f"2. Click 'GET /ask', then 'Try it out', then 'Execute'\n")
   
   uvicorn.run(app, host="0.0.0.0", port=8000)
#config =uvicorn.Config(app, host="0.0.0.0", port=8000)
#server = uvicorn.Server(config)

#asyncio.get_event_loop().create_task(server.serve())
