#/usr/bin/python
# -*- coding: utf-8 -*-
#########################
# Fonctions pour appsnmp#
# Karim Ayari           #
# DSI                   #
# Rectorat de Lyon      #
#########################


def getsnmp(iprouteur):
    """
    Récupere les informations sur le routeur en snmp
    """
    from commands import getoutput

    community=""
    
    ref=getoutput("snmpwalk -v2c -c %s %s sysName.0 |awk -F\"=\" '{print $2}' |awk -F\":\" '{print $2}'|awk -F\"-\" '{print $1}'" % (community,iprouteur)).replace(' ','')
    lbb=getoutput("snmpwalk -v2c -c %s %s sysName.0 |awk -F\"=\" '{print $2}' |awk -F\":\" '{print $2}'|awk -F\"-\" '{print $2}'" % (community,iprouteur)).replace(' ','')
    ip=getoutput("snmpwalk -v2c -c %s %s SNMPv2-SMI::mib-2.15.4.0 |awk -F\"=\" '{print $2}' |awk -F\":\" '{print $2}'" % (community,iprouteur)).replace(' ','')
    upt="#upt "+getoutput("snmpwalk -v2c -c %s %s sysUpTimeInstance |awk -F\"=\" '{print $2}' |awk '{print $3\" \"$4\" \"$5}'" % (community,iprouteur)).replace('#upt','')
    return ref,lbb,ip,upt
	

def basetab(ip):
    """
    Connexion a la base de donnees
    """
    from MySQLdb import connect

    # Open database connection
    db = connect("localhost","login","mdp","bd" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # execute SQL query using execute() method.
    cursor.execute("SELECT idLien,ip_gw,ref_operateur,ip_routeur_lo,nom,Type_Routeur from amon where ip_gw like '%s'" % ip)
    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    # disconnect from server
    db.close()
    return data


def fping(ipsup):
    """
    Test de la supervision du routeur
    """
    from commands import getstatusoutput

    state_ping,y=getstatusoutput('fping %s' % ipsup)
    return state_ping
