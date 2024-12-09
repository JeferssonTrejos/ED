from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Mascotas(Base):
    __tablename__ = 'tbl_mascota'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    raza = Column(String, nullable=False)
    dueño_id = Column(Integer, ForeignKey('tbl_dueño.id'), nullable=False)

class Dueños(Base):
    __tablename__ = 'tbl_dueño'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    telefono = Column(String, nullable=True)

class VisitasVeterinarias(Base):
    __tablename__ = 'tbl_visita_veterinaria'
    
    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    motivo = Column(String, nullable=False)
    mascota_id = Column(Integer, ForeignKey('tbl_mascota.id'), nullable=False)

engine = create_engine('sqlite:///veterianria.db', echo=True)
Base.metadata.create_all(engine)
