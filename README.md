Dynamic Certificate Generator
==============================

What Is This?
-------------

This is an simple yet amazing set of python program to build awesome certificates at runtime.

* Single Certificate Geneation
* Bulk Certificate Generation

Pre-requisites
--------------

* Python 2.7 or later version.
* Required Python Packages: sys, json, pandas, pillow, mathplotlib.

Steps to generate certificate
--------------
1. Copy the certificate with unique name in the *certificates* folder.
2. Run genConfigfile.py with 2 parameters
    * certificate name with extension.
    * Total number of text fields. 
3. Open the *configs* folder and update values in *certificateUID.json*
4. Run getCoordinates.py with 1 parameter *certificateUID*  to open a plotted window.
5. Use mouse cursor to find co-ordinates of text fields and update in config file.
6. Run genCertificate.py with 1 parameter to generate certificates usig config file.
    * Single - Pass required values at run time.
    * BulK - Pass dataSheet name to generate certificates.

Demo
---------------

Development
-----------

If you want to work on this application we’d love your pull requests and tickets on GitHub!

1. If you open up a ticket, please make sure it describes the problem or feature request fully.
2. If you send us a pull request, make sure you add a test for what you added.