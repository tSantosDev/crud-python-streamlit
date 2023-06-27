import services.database as db;
import models.venda as venda;

def incluirVenda(venda):
    count = db.cursor.execute("""
    INSERT INTO venda (bomba_id, combustivel_id, quantidade_venda) 
    VALUES (?,?,?)""",
    venda.bomba_id, venda.combustivel_id, venda.quantidade_venda).rowcount
    db.cnxn.commit()

def selecionarIdVenda(venda_id):
    db.cursor.execute("SELECT * FROM venda WHERE venda_id = ?", venda_id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(venda.venda(row[0], row[1], row[2], row[3]))

    return costumerList[0]      

def alterarVenda(venda):
    count = db.cursor.execute("""
    UPDATE venda 
    SET bomba_id = ?, combustivel_id = ?, quantidade_venda = ?
    WHERE venda_id = ?""",
    venda.bomba_id, venda.combustivel_id, venda.quantidade_venda, venda.venda_id).rowcount
    db.cnxn.commit()

def excluirVenda(venda_id):
    count = db.cursor.execute("""
    DELETE FROM venda WHERE venda_id = ?""",
    venda_id).rowcount
    db.cnxn.commit()

def selecionarVenda():
    db.cursor.execute("SELECT * FROM venda")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(venda.venda(row[0], row[1], row[2], row[3]))

    return costumerList    