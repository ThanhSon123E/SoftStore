from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Software(db.Model):
    __tablename__ = 'softwares'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    version = db.Column(db.String(50), nullable=False, default='1.0.0')
    description = db.Column(db.String(255), nullable=False)
    detail_description = db.Column(db.Text, nullable=True)
    category = db.Column(db.String(50), nullable=False) # browsers, dev, office, design, utilities, games, security
    developer = db.Column(db.String(100), nullable=False)
    file_size = db.Column(db.String(20), nullable=False, default='10 MB')
    download_count = db.Column(db.Integer, default=0)
    icon_type = db.Column(db.String(50), nullable=False)  # Tên icon SVG để hiển thị động
    download_filename = db.Column(db.String(100), nullable=False)
    download_url = db.Column(db.String(255), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'version': self.version,
            'description': self.description,
            'category': self.category,
            'developer': self.developer,
            'file_size': self.file_size,
            'download_count': self.download_count,
            'icon_type': self.icon_type,
            'download_filename': self.download_filename,
            'download_url': self.download_url,
            'versions': [{'version': v.version, 'file_size': v.file_size, 'download_url': v.download_url} for v in self.versions]
        }

class SoftwareVersion(db.Model):
    __tablename__ = 'software_versions'
    
    id = db.Column(db.Integer, primary_key=True)
    software_id = db.Column(db.Integer, db.ForeignKey('softwares.id', ondelete='CASCADE'), nullable=False)
    version = db.Column(db.String(50), nullable=False)
    download_url = db.Column(db.String(255), nullable=False)
    file_size = db.Column(db.String(20), nullable=False, default='10 MB')
    
    # Thiết lập quan hệ ngược lại
    software = db.relationship('Software', backref=db.backref('versions', lazy=True, cascade='all, delete-orphan'))
