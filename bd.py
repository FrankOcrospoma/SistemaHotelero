import pymysql

def obtener_conexion():
    return pymysql.connect(host='viaduct.proxy.rlwy.net',
                                port=36033,
                                user='root',
                                password='bgCHCddhcBfe12ccHDf14AFHccbD4E-a',
                                db='hotel')