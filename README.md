# TCRpdbTools
Web application for processing T-cell Receptor (TCR) structural files (PDBs) with visual reference.

## Installation
This program is setup to run in a docker container. Ensure that docker is installed on your system. The rest of the requirements will be installed when building. Look into "requirements.txt" for details on other installs.

```bash
docker compose build
```

## Getting Started
To run my awesome app simply,
```bash
docker comopose up
```
Visit (http://localhost:8000) in your browser of choice.

### Example Use
1. I recommend downloading a free protein viewer software. The one I'd suggest is UCSF Chimera. You can find the download [here](https://www.cgl.ucsf.edu/chimera/download.html).

2. Select a PDB from the drop-down selection. Go ahead and click "submit". (2vlk, 3gsn are two of my go-to's)

3. Look at this file using the installed protein viewer software.

4. Now we're going to perform a modification. Select the same PDB from the drow-down and now for action 1 perform "Trim TCR". For action 2 select "Center". Then go ahead and click "Submit".

5. Inspect the modified structure. What you'll see are now just two protein chains versus several, these are the alpha and beta chains of a TCR. We trimmed them to just the variable region. We also centered the coordinates of the variable region to position 0,0,0 in 3D space and aligned the principle axes of inertia along the X, Y, and Z axes. 

## User Stories
As a student, I want to be able to easily access T-cell Receptor structural data from a list of existing public PDB file, so that I can visualize the protein structures in a 3D viewer.



As a structural biologist, I want to be able to easily upload T-cell Receptor structural data stored as a PDB, so that I can conduct modifications that can help further analysis.



As an administrator, I want to be able to view statical data on cite traffic, so I can share this data with other researchers when describing the usefulness of the application.



As a mis-user, I want to collect structural biologist data of T-cell Receptors that may not be published yet in a public database.

Response: Ensure that proper security measures are in place to prevent access to other users' accounts. Several steps can be in place, non-plain text storage of passwords, captcha if several attempts, and potential for 2FA.

As a mis-user, I want to collect information stored about other users such as email and password, so I can cross-reference with other accounts the user may have on other cites.

Response: Ensure that data stored on users is saved in a proper manner and avoiding any form of attach that gives access to user information.

## Diagrams

### Mockup
![alt text](https://github.com/aseamann/tcr-pdb-tools/blob/main/WebpageDesign.png?raw=true)

### Architecture Diagrams
![alt text](https://github.com/aseamann/tcr-pdb-tools/blob/main/TCRpdbToolsDiagram.png?raw=true)

# License
The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
