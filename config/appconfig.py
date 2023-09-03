def init_app(app):
    app.config['PORT'] = 4567
    app.config['IMAGE'] = 'seqserv-with-customisations'
    app.config['DATABASE'] = r'/home/savio-miranda/Documentos/UFPA-CC-2023/Labiocad/database-bioinfo/teste'
    app.config['INDEX'] = r'http://localhost:4567'