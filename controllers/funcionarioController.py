import services.database as db;
import models.funcionario as funcionario;

def incluirFuncionario(funcionario):
    count = db.cursor.execute("""
    INSERT INTO funcionario (nome_funcionario, CPF) 
    VALUES (?,?)""",
    funcionario.nome_funcionario, funcionario.CPF).rowcount
    db.cnxn.commit()

def selecionarIdFuncionario(funcionario_id):
    db.cursor.execute("SELECT * FROM funcionario WHERE funcionario_id = ?", funcionario_id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(funcionario.funcionario(row[0], row[1], row[2]))

    return costumerList[0]      

def alterarFuncionario(funcionario):
    count = db.cursor.execute("""
    UPDATE funcionario 
    SET nome_funcionario = ?, CPF = ?
    WHERE funcionario_id = ?""",
    funcionario.nome_funcionario, funcionario.CPF, funcionario.funcionario_id).rowcount
    db.cnxn.commit()    

def excluirFuncionario(funcionario_id):
    count = db.cursor.execute("""
    DELETE FROM funcionario WHERE funcionario_id = ?""",
    funcionario_id).rowcount
    db.cnxn.commit()

def selecionarFuncionario():
    db.cursor.execute("SELECT * FROM funcionario")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(funcionario.funcionario(row[0], row[1], row[2]))

    return costumerList    