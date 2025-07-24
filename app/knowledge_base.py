import os
import json
from typing import List, Dict, Any, Optional
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document

from config import settings


class SimpleKnowledgeBase:
    """Simple knowledge base for testing without vector database."""
    
    def __init__(self):
        self.knowledge_items = []
        self.initialize_sample_data()
    
    def initialize_sample_data(self):
        """Initialize with sample knowledge base data."""
        sample_data = [
            {
                "title": "How to Reset Password",
                "content": """
                To reset your password, follow these steps:
                1. Go to the login page
                2. Click on "Forgot Password"
                3. Enter your email address
                4. Check your email for a reset link
                5. Click the link and enter a new password
                6. Confirm your new password
                
                If you don't receive the email, check your spam folder or contact support.
                """,
                "category": "account",
                "tags": ["password", "reset", "login", "security"]
            },
            {
                "title": "Product Return Policy",
                "content": """
                Our return policy allows returns within 30 days of purchase:
                
                - Items must be in original condition
                - Original packaging required
                - Return shipping is free for defective items
                - Refunds processed within 5-7 business days
                
                To initiate a return:
                1. Log into your account
                2. Go to Order History
                3. Select the item to return
                4. Print return label
                5. Ship item back
                
                Contact us if you have any questions about returns.
                """,
                "category": "returns",
                "tags": ["return", "refund", "policy", "shipping"]
            },
            {
                "title": "Payment Methods",
                "content": """
                We accept the following payment methods:
                
                Credit/Debit Cards:
                - Visa
                - Mastercard
                - American Express
                - Discover
                
                Digital Wallets:
                - PayPal
                - Apple Pay
                - Google Pay
                
                Other:
                - Bank transfers (for business accounts)
                - Gift cards
                
                All payments are processed securely through our payment partners.
                """,
                "category": "payment",
                "tags": ["payment", "credit card", "paypal", "apple pay"]
            },
            {
                "title": "Shipping Information",
                "content": """
                Shipping options and delivery times:
                
                Standard Shipping (3-5 business days):
                - Free for orders over $50
                - $5.99 for orders under $50
                
                Express Shipping (1-2 business days):
                - $12.99 for all orders
                
                Overnight Shipping:
                - $25.99 for all orders
                
                International Shipping:
                - Available to select countries
                - 7-14 business days
                - Additional customs fees may apply
                
                Track your order through your account or with the tracking number provided.
                """,
                "category": "shipping",
                "tags": ["shipping", "delivery", "tracking", "international"]
            },
            {
                "title": "Account Security",
                "content": """
                Keep your account secure with these tips:
                
                Password Security:
                - Use a strong, unique password
                - Enable two-factor authentication
                - Never share your password
                
                Account Monitoring:
                - Regularly review your order history
                - Check for unauthorized activity
                - Update your contact information
                
                If you suspect unauthorized access:
                1. Change your password immediately
                2. Contact customer support
                3. Review recent account activity
                
                We use industry-standard encryption to protect your data.
                """,
                "category": "security",
                "tags": ["security", "password", "two-factor", "encryption"]
            }
        ]
        
        for item in sample_data:
            self.knowledge_items.append(item)
    
    def search(self, query: str, k: int = 5, category: Optional[str] = None) -> List[Dict[str, Any]]:
        """Simple keyword-based search."""
        query_lower = query.lower()
        results = []
        
        for item in self.knowledge_items:
            if category and item["category"] != category:
                continue
                
            # Simple keyword matching
            content_lower = item["content"].lower()
            title_lower = item["title"].lower()
            
            # Check if query keywords are in content or title
            query_words = query_lower.split()
            matches = 0
            
            for word in query_words:
                if word in content_lower or word in title_lower:
                    matches += 1
            
            if matches > 0:
                # Calculate simple relevance score
                relevance = matches / len(query_words)
                results.append({
                    "content": item["content"][:500] + "..." if len(item["content"]) > 500 else item["content"],
                    "metadata": {
                        "title": item["title"],
                        "category": item["category"],
                        "tags": item["tags"]
                    },
                    "score": relevance
                })
        
        # Sort by relevance and return top k
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:k]
    
    def add_document(self, title: str, content: str, category: str, tags: List[str] = None) -> str:
        """Add a document to the knowledge base."""
        doc_id = f"doc_{len(self.knowledge_items)}"
        self.knowledge_items.append({
            "id": doc_id,
            "title": title,
            "content": content,
            "category": category,
            "tags": tags or []
        })
        return doc_id
    
    def get_all_documents(self) -> List[Dict[str, Any]]:
        """Get all documents from the knowledge base."""
        return self.knowledge_items


class KnowledgeBaseManager:
    """Knowledge base manager that uses simple search for now."""
    
    def __init__(self):
        self.simple_kb = SimpleKnowledgeBase()
        # Create a mock vectorstore for compatibility
        self.vectorstore = MockVectorStore(self.simple_kb)
    
    def add_document(self, title: str, content: str, category: str, tags: List[str] = None) -> str:
        """Add a document to the knowledge base."""
        return self.simple_kb.add_document(title, content, category, tags)
    
    def search(self, query: str, k: int = 5, category: Optional[str] = None) -> List[Dict[str, Any]]:
        """Search the knowledge base."""
        return self.simple_kb.search(query, k, category)
    
    def get_all_documents(self) -> List[Dict[str, Any]]:
        """Get all documents from the knowledge base."""
        return self.simple_kb.get_all_documents()


class MockVectorStore:
    """Mock vector store for compatibility with LangChain."""
    
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
    
    def as_retriever(self, search_type="similarity", search_kwargs=None):
        return MockRetriever(self.knowledge_base)


class MockRetriever:
    """Mock retriever that uses simple search."""
    
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
    
    def get_relevant_documents(self, query: str):
        results = self.knowledge_base.search(query, k=3)
        documents = []
        
        for result in results:
            doc = Document(
                page_content=result["content"],
                metadata=result["metadata"]
            )
            documents.append(doc)
        
        return documents


def initialize_knowledge_base():
    """Initialize the knowledge base."""
    kb_manager = KnowledgeBaseManager()
    print("Knowledge base initialized successfully!")
    return kb_manager 