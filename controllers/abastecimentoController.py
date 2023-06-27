import services.database as db;
import models.abastecimento as abastecimento;

def incluirAbastecimento(abastecimento):
    count = db.cursor.execute("""
    INSERT INTO abastecimento (combustivel_id, quantidade_abastecimento) 
    VALUES (?,?)""",
    abastecimento.combustivel_id, abastecimento.quantidade_abastecimento).rowcount
    db.cnxn.commit()

def selecionarIdAbastecimento(abastecimento_id):
    db.cursor.execute("SELECT * FROM abastecimento WHERE abastecimento_id = ?", abastecimento_id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(abastecimento.abastecimento(row[0], row[1], row[2]))

    return costumerList[0]      

def alterarAbastecimento(abastecimento):
    count = db.cursor.execute("""
    UPDATE abastecimento 
    SET combustivel_id = ?, quantidade_abastecimento = ?
    WHERE abastecimento_id = ?""",
    abastecimento.combustivel_id, abastecimento.quantidade_abastecimento, abastecimento.abastecimento_id).rowcount
    db.cnxn.commit()    

def excluirAbastecimento(abastecimento_id):
    count = db.cursor.execute("""
    DELETE FROM abastecimento WHERE abastecimento_id = ?""",
    abastecimento_id).rowcount
    db.cnxn.commit()

def selecionarAbastecimento():
    db.cursor.execute("SELECT * FROM abastecimento")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(abastecimento.abastecimento(row[0], row[1], row[2]))

    return costumerList