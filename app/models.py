from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base

class TestCase(Base):
    __tablename__ = "test_cases"
    id = Column(Integer, primary_key=True)
    name = Column(String(180), nullable=False)
    test_type = Column(String(20), nullable=False)
    endpoint = Column(String(300), default="")
    description = Column(String(500), default="")
    status = Column(String(20), default="Active")
    created_at = Column(DateTime, default=datetime.utcnow)

class TestRun(Base):
    __tablename__ = "test_runs"
    id = Column(Integer, primary_key=True)
    suite = Column(String(40), nullable=False)
    status = Column(String(20), nullable=False)
    total = Column(Integer, default=0)
    passed = Column(Integer, default=0)
    failed = Column(Integer, default=0)
    duration = Column(Float, default=0)
    report = Column(String(300), default="")
    started_at = Column(DateTime, default=datetime.utcnow)

class TestResult(Base):
    __tablename__ = "test_results"
    id = Column(Integer, primary_key=True)
    run_id = Column(Integer, nullable=False)
    test_name = Column(String(250), nullable=False)
    test_type = Column(String(20), nullable=False)
    status = Column(String(20), nullable=False)
    duration = Column(Float, default=0)
    message = Column(String(800), default="")
    created_at = Column(DateTime, default=datetime.utcnow)
