from fastapi import APIRouter, HTTPException
from app.models.terms import TermsContent

router = APIRouter(prefix="/terms", tags=["Terms and Conditions"])

# In-memory storage for terms content
_terms_text = {
    "content": "Default terms and conditions content here..."
}

@router.get("/", response_model=TermsContent)
def get_terms():
    return TermsContent(content=_terms_text["content"])

@router.post("/")
def update_terms(terms: TermsContent):
    _terms_text["content"] = terms.content
    return {"message": "Terms and Conditions updated successfully."}
