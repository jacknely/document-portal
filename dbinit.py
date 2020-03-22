from app.models import *

db.create_all()

# Sample Data...

part1 = PartNumber("01234")
db.session.add(part1)

supplier1 = Supplier("Test1")
db.session.add(supplier1)

build_phase1 = BuildPhase("Phase 1")
db.session.add(build_phase1)


db.session.commit()
