# WLST Offline for deploying an application under APP_NAME packaged in APP_PKG_FILE located in APP_PKG_LOCATION
# It will read the domain under DOMAIN_HOME by default
# =============================
import os

# Deployment Information 
domainname = os.environ.get('DOMAIN_NAME', 'base_domain')
domainhome = os.environ.get('DOMAIN_HOME', '/u01/oracle/user_projects/domains/' + domainname)
cluster_name = os.environ.get("CLUSTER_NAME", "DockerCluster")

# Read Domain in Offline Mode
readDomain(domainhome)

# Create Datasource
print 'create JDBCSystemResource'
create(dsname, 'JDBCSystemResource')
cd('/JDBCSystemResource/' + dsname + '/JdbcResource/' + dsname)
cmo.setName(dsname)
 
cd('/JDBCSystemResource/' + dsname + '/JdbcResource/' + dsname)
create('myJdbcDataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
set('JNDIName', java.lang.String(dsjndiname))
set('GlobalTransactionsProtocol', java.lang.String('None'))
 
cd('/JDBCSystemResource/' + dsname + '/JdbcResource/' + dsname)
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName', dsdriver)
set('URL', dsurl)
set('PasswordEncrypted', dspassword)
set('UseXADataSourceInterface', 'false')
 
print 'create JDBCDriverParams Properties'
create('myProperties','Properties')
cd('Properties/NO_NAME_0')
create('user','Property')
cd('Property/user')
set('Value', dsusername)

print 'create JDBCConnectionPoolParams'
cd('/JDBCSystemResource/' + dsname + '/JdbcResource/' + dsname)
create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
cd('JDBCConnectionPoolParams/NO_NAME_0')
set('TestTableName','SQL SELECT 1 FROM DUAL')

# Assign
assign('JDBCSystemResource', dsname, 'Target', 'AdminServer')
assign('JDBCSystemResource', dsname, 'Target', cluster_name)

# Update Domain, Close It, Exit
updateDomain()
closeDomain()
exit()