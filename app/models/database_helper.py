import sys,os
from flask_sqlalchemy import SQLAlchemy
from config import load_config

APP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(APP_ROOT)

from app.models.database import db  

class DatabaseHelper:


    @staticmethod
    def add_record(model, **kwargs):
        """Generic method to add a record to the database."""
        try:
            # Create an instance of the specified model class with provided attributes
            record = model(**kwargs)
            db.session.add(record)
            db.session.commit()
            return record.to_dict()
        except Exception as e:
            db.session.rollback()
            print(f"Error adding record: {e}")
            return None


    @staticmethod
    def delete_record(model, record_id):
        """Delete a record from the database by ID."""
        try:
            record = model.query.get(record_id)
            if record:
                db.session.delete(record)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting record: {e}")
            return False

    @staticmethod
    def update_record(record, updates: dict):
        """Update a record with the given updates dictionary."""
        try:
            for key, value in updates.items():
                setattr(record, key, value)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error updating record: {e}")
            return False

    @staticmethod
    def get_record_by_id(model, record_id):
        """Fetch a record by ID."""
        return model.query.get(record_id)

    @staticmethod
    def get_records(model, **filters):
        """
        Fetch records of a model with optional filter conditions.

        :param model: The model to query.
        :param filters: Keyword arguments representing the filter conditions.
        :return: A list of matching records.
        """
        query = model.query
        if filters:
            query = query.filter_by(**filters)
        return query.all()

    @staticmethod
    def delete_record(model, record_id):
    """
    Permanently delete a record from the database.
    
    :param model: The model class to delete from.
    :param record_id: The ID of the record to delete.
    :return: True if the record was found and deleted, False otherwise.
    """
    record = model.query.get(record_id)
    if record:
        db.session.delete(record)
        db.session.commit()
        return True
    return False

    @staticmethod
    def soft_delete_record(model, record_id):
        """Soft delete a record (assumes `is_deleted` column)."""
        try:
            record = model.query.get(record_id)
            if record and hasattr(record, 'is_deleted'):
                record.is_deleted = True
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            print(f"Error in soft deleting record: {e}")
            return False
