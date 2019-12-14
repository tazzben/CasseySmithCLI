# CasseySmith
 
A command line tool to generate the null hypothesis distributions for the Ellison-Glaeser index.  This is a modernization of the command line tool released with [Cassey and Smith (2014)](http://doi.org/10.1016/j.jue.2014.02.005).

## Examples:

The user specifies to simulate combinations of 20 and 30 plants per industry: 

~~~

./CasseySmith 20 30

~~~

The user specifies critical values:

~~~

./CasseySmith 20 30 --criticalValues 0.05 0.95

~~~

The user specifies specific sigma values:

~~~

./CasseySmith 20 30 --criticalValues 0.05 0.95 --sigma 1.0 1.5

~~~

The user specifies a text file containing state population weights:

~~~

./CasseySmith 20 30 --criticalValues 0.05 0.95 --sigma 1.0 1.5 --states statefile.txt

~~~

This tool is built using [CasseySmithCV package](https://github.com/tazzben/CasseySmithCV).  However, it does not require the installation of python.  Pre-packaged builds of the software for Windows and macOS are available in the releases section.