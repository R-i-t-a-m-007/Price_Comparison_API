from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .models import Product
from .database import SessionLocal, engine, Base
from .schemas import ProductCreate, ProductResponse
import json

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Price Comparison API"}

@app.get("/api/products", response_model=list[ProductResponse])
def get_products(name: str = None, db: Session = Depends(get_db)):
    if name:
        products = db.query(Product).filter(Product.name.ilike(f"%{name}%")).all()
    else:
        products = db.query(Product).all()
    return products

@app.post("/api/products", response_model=ProductResponse)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(name=product.name, price=product.price, retailer_name=product.retailer_name)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def init_db(db: Session):
    with open("data/mock_data.json") as f:
        data = json.load(f)
        for retailer, products in data.items():
            for product in products:
                db_product = Product(name=product["name"], price=product["price"], retailer_name=retailer)
                db.add(db_product)
        db.commit()

# Initialize database with mock data if empty
@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    if db.query(Product).count() == 0:
        init_db(db)
    db.close()
