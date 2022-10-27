# TCRpdbTools
Web application for processing T-cell Receptor (TCR) structural files (PDBs) with visual reference.

## Installation
```bash
docker-build .
docker-compose run django bash
python manage.py migrate
python manage.py createsuperuser
```

## Getting Started
To run my awesome app simply,
```bash
###### docker-compose up
docker run -it -p 8020:8020 \
-e DJANGO_SUPERUSER_USERNAME=admin \
-e DJANGO_SUPERUSER_PASSWORD=password \
-e DJANGO_SUPERUSER_EMAIL=admin@example.com \
tcr-pdb-tools
```
See in-app menus for help with using specific features.

## User Stories
As a student, I want to be able to easily access T-cell Receptor structural data from a list of existing public PDB file, so that I can visualize the protein structures in a 3D viewer.



As a structural biologist, I want to be able to easily upload T-cell Receptor structural data stored as a PDB, so that I can conduct modifications that can help further analysis.



As an administrator, I want to be able to view statical data on cite traffic, so I can share this data with other researchers when describing the usefulness of the application.



As a mis-user, I want to collect structural biologist data of T-cell Receptors that may not be published yet in a public database.

Ensure that proper security measures are in place to prevent access to other users' accounts. Several steps can be in place, non-plain text storage of passwords, captcha if several attempts, and potential for 2FA.

As a mis-user, I want to ....

## Diagrams

### Mockup
![alt text](https://github.com/aseamann/tcr-pdb-tools/blob/main/WebpageDesign.png?raw=true)

### Architecture Diagrams

# License
The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
