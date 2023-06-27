import services.database as db;
import models.bomba as bomba;

def incluirBomba(bomba):
    count = db.cursor.execute("""
    INSERT INTO bomba (combustivel_id) 
    VALUES (?)""",
    bomba.combustivel_id).rowcount
    db.cnxn.commit()

def selecionarIdBomba(bomba_id):
    db.cursor.execute("SELECT * FROM bomba WHERE bomba_id = ?", bomba_id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(bomba.bomba(row[0], row[1]))

    return costumerList[0]      

def alterarBomba(bomba):
    count = db.cursor.execute("""
    UPDATE bomba 
    SET combustivel_id = ?
    WHERE bomba_id = ?""",
    bomba.combustivel_id, bomba.bomba_id).rowcount
    db.cnxn.commit()    

def excluirBomba(bomba_id):
    count = db.cursor.execute("""
    DELETE FROM bomba WHERE bomba_id = ?""",
    bomba_id).rowcount
    db.cnxn.commit()

def selecionarBomba():
    db.cursor.execute("SELECT * FROM bomba")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(bomba.bomba(row[0], row[1]))

    return costumerList    