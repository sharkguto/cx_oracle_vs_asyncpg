#!/bin/sh
#
# $Header: odbc/utl/odbc_update_ini.sh.pp.repos /main/24 2017/10/19 16:01:53 tianfyan Exp $
#
# odbc_update_ini.sh
#
# Copyright (c) 2005, 2017, Oracle and/or its affiliates. All rights reserved.
#
#    NAME
#      odbc_update_ini.sh 
#       - updates <DM-HOME>/etc/odbcinst.ini and ~/.odbc.ini
#
#    DESCRIPTION
#      Usage: odbc_update_ini.sh <ODBCDM_HOME> 
#                            [<Install-location>] [Driver-name>] [<DSN>] [<ODBCINI>]
#      The script should be run from the directory where ODBC driver .so is
#      available if installation location is not passed as arg-2.
#
#    NOTES
#      <other useful comments, qualifications, etc.>
#
#    MODIFIED   (MM/DD/YY)
#    tianfyan    10/10/17 - Replaced hard-coded version number with a
#                           substitution for the version.
#    tianfyan    06/19/17 - ER-19541554: Added 'LobPrefetchSize' option
#    bhshanmu    05/05/17 - bhshanmu_bug-26003322_linux
#    akumarb     06/25/15 - Fix for LRG#12951028
#    akumarb     03/21/14 - Changes for CDB Concurrent Framework
#    ksowmya     02/26/13 - ER[16096713] Adding 'AggregateSQLType' odbc.ini
#                           option
#    ksowmya     12/05/12 - Update version to 12.1
#    ksowmya     07/11/12 - Bug[14307758]Removing 'EnableImplicitResults'
#                           odbc.ini option
#    ksowmya     12/12/11 - Bug[12905310]Remove SQLTranslationProfile option.We
#                           don't support that any more.
#    ksowmya     05/30/11 - Proj#37050, Implicit results
#    ksowmya     04/04/11 - Babelfish proj#33351
#    ksowmya     04/14/09 - Bug[7704827]Support for 'UseOCIDescribeAny' flag in
#                           odbc.ini
#    akapila     04/17/08 - modified for bug-6915027.
#    akapila     09/03/07 - modified for bug-6374802.
#    akapila     11/09/06 - modified for bug-5348587.
#    akapila     05/17/06 - 
#    ardesai     11/23/05 - 
#    ardesai     11/23/05 - 
#    ardesai     11/23/05 - 
#    ardesai     11/23/05 - 
#    akapila     03/06/06 - modified for bug-4150034. 
#    akapila     09/26/05 - modified for bug4608183. 
#    subanerj    09/16/05 - Fixed bug 4557506. Added optional arguments.
#    ardesai     05/31/05 - ardesai_bug-4397895
#    ardesai     05/28/05 - Creation
#
# =========================================================================

# ODBCDM_HOME needs to be passed as arg-1
if [ ! "$1" ]
then
   echo " *** Please pass ODBCDM_HOME as arg-1, and optional arguments -"
   echo " *** Install location (arg-2), Driver name (arg-3) & DSN (arg-4) & ODBCINI (arg-5)."
   echo " *** Usage:  odbc_update_ini.sh <ODBCDM_Home> [<Install_Location>] [<Driver_Name>] [<DSN>] [<ODBCINI>]"
   exit
else
   ODBCDM_HOME="$1"
fi

# Check whether Driver Manager is installed or not
if [ ! -f  $ODBCDM_HOME/etc/odbc.ini  -o  ! -f $ODBCDM_HOME/etc/odbcinst.ini ]
then
   echo " *** INI file not found. Driver Manager not installed!"
   exit
fi

# Add driver entry in $ODBCDM_HOME/etc/odbcinst.ini file
#
DRIVER_DESCRIPTION="Oracle ODBC driver for Oracle 19"

# If a driver location is passed, use that or use the current directory
if [ ! "$2" ]
     then
        DRIVER_LOCATION=`pwd`
     else
        DRIVER_LOCATION="$2"
fi

# Check for Driver name
if [ ! "$3" ]
     then
        DRIVER_NAME="Oracle 19 ODBC driver"
     else
        DRIVER_NAME="$3"
fi

# ODBCINI environment variable is the location of .odbc.ini,if not passed 
#then default is $HOME/.odbc.ini
if [ ! "$5" ]
then
    echo " *** ODBCINI environment variable not set,defaulting it to HOME directory!"
    ODBCINI_PATH=$HOME/.odbc.ini
else
    ODBCINI_PATH="$5"
fi

# We know driver .so name 
SO_NAME=libsqora.so.19.1

echo "
[$DRIVER_NAME]
Description     = $DRIVER_DESCRIPTION
Driver          = $DRIVER_LOCATION/$SO_NAME
Setup           =
FileUsage       =
CPTimeout       =
CPReuse         = " >> $ODBCDM_HOME/etc/odbcinst.ini
			      
# Add DSN entry 
# If a DSN name is passed, use that or use the default name
if [ ! "$4" ]
     then
        DSN="OracleODBC-19"
     else
        DSN="$4"
fi
			      
echo "
[$DSN]
AggregateSQLType = FLOAT
Application Attributes = T
Attributes = W
BatchAutocommitMode = IfAllSuccessful
BindAsFLOAT = F
CacheBufferSize = 20
CloseCursor = F
DisableDPM = F
DisableMTS = T
DisableRULEHint = T
Driver = $DRIVER_NAME
DSN = $DSN
EXECSchemaOpt =
EXECSyntax = T
Failover = T
FailoverDelay = 10
FailoverRetryCount = 10
FetchBufferSize = 64000
ForceWCHAR = F
LobPrefetchSize = 8192
Lobs = T
Longs = T
MaxLargeData = 0
MaxTokenSize = 8192
MetadataIdDefault = F
QueryTimeout = T
ResultSets = T
ServerName = 
SQLGetData extensions = F
SQLTranslateErrors = F
StatementCache = F
Translation DLL =
Translation Option = 0
UseOCIDescribeAny = F
UserID = 
"  >> $ODBCINI_PATH

# Add DSN entry in "ODBC Data Sources" list
#
cat $ODBCINI_PATH | sed "s/\[ODBC Data Sources\]/\[ODBC Data Sources\]\n$DSN = $DRIVER_DESCRIPTION/g" > odbc.ini
mv odbc.ini $ODBCINI_PATH

