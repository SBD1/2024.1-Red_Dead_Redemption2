from multiprocessing import connection
import psycopg2
from classes import *


class DataBase():

    def create_connection(self):
        connect = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres")
        return connect

    def create_new_map(connection, nome):
        cursor = connection.cursor()

        query = "INSERT INTO mapa (nome) VALUES ('%s')" % (nome)

        cursor.execute(query)
        connection.commit()
        cursor.close()

    def create_new_state(connection, idMapa, nome, sigla, descricao):
        cursor = connection.cursor()

        query = """INSERT INTO estado (idMapa, nome, sigla, descricao) 
                VALUES (%s, '%s', '%s', '%s')""" % (idMapa, nome, sigla, descricao)

        cursor.execute(query)
        connection.commit()
        cursor.close()

    def get_map(connection, nome):
        cursor = connection.cursor()

        query = "SELECT * FROM mapa WHERE nome = '%s'" % (nome)
        
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()

        return result

    def get_state(connection, sigla):
        cursor = connection.cursor()

        query = "SELECT * FROM estado WHERE sigla = '%s'" % (sigla)
        
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()

        return result

    def create_new_player(connection, idPersonagem, idInventario, idCidade, idClasse, idGangue, nome, username, senha_hash):
        cursor = connection.cursor()

        query = """INSERT INTO jogador (
                    idPersonagem, idInventario, idCidade, idClasse, idGangue, nome, xp, dinheiro, 
                    velocidade, vidaMax, vidaAtual, staminaMax, staminaAtual, username, senha_hash
                ) VALUES (%s, %s, %s, %s, %s, %s, 0, 0, 7, 100, 100, 1000, 1000, %s, %s)"""

        values = (idPersonagem, idInventario, idCidade, idClasse, idGangue, nome, username, senha_hash)

        cursor.execute(query, values)
        connection.commit()
        cursor.close()

    def get_player_by_username(connection, username):
        cursor = connection.cursor()

        query = "SELECT * FROM jogador WHERE username = %s"
        
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()

        return result

    def update_player_stats(connection, idPersonagem, xp=None, dinheiro=None, vidaAtual=None, staminaAtual=None):
        cursor = connection.cursor()

        updates = []
        values = []

        if xp is not None:
            updates.append("xp = %s")
            values.append(xp)
        if dinheiro is not None:
            updates.append("dinheiro = %s")
            values.append(dinheiro)
        if vidaAtual is not None:
            updates.append("vidaAtual = %s")
            values.append(vidaAtual)
        if staminaAtual is not None:
            updates.append("staminaAtual = %s")
            values.append(staminaAtual)
        
        if updates:
            update_clause = ", ".join(updates)
            query = "UPDATE jogador SET %s WHERE idPersonagem = %s" % (update_clause, "%s")
            values.append(idPersonagem)

            cursor.execute(query, values)
            connection.commit()
        
        cursor.close()

    def create_regiao(self, regiao):
        with self.connection.cursor() as cursor:
            query = """
                INSERT INTO regiao (idMapa, nome, descricao) 
                VALUES (%s, %s, %s)
                RETURNING idRegiao;
            """
            cursor.execute(query, (regiao.idMapa, regiao.nome, regiao.descricao))
            regiao_id = cursor.fetchone()[0]
            self.connection.commit()
            return regiao_id

    def get_regiao(self, id_regiao):
        with self.connection.cursor() as cursor:
            query = """
                SELECT idRegiao, idMapa, nome, descricao 
                FROM regiao
                WHERE idRegiao = %s;
            """
            cursor.execute(query, (id_regiao,))
            result = cursor.fetchone()
            if result:
                return Regiao(*result)
            else:
                return None

    def update_regiao(self, regiao):
        with self.connection.cursor() as cursor:
            query = """
                UPDATE regiao
                SET idMapa = %s, nome = %s, descricao = %s
                WHERE idRegiao = %s;
            """
            cursor.execute(query, (regiao.idMapa, regiao.nome, regiao.descricao, regiao.idRegiao))
            self.connection.commit()

    def create_sala(self, sala):
        with self.connection.cursor() as cursor:
            query = """
                INSERT INTO sala (idRegiao, nome, descricao)
                VALUES (%s, %s, %s)
                RETURNING idSala;
            """
            cursor.execute(query, (sala.idRegiao, sala.nome, sala.descricao))
            sala_id = cursor.fetchone()[0]
            self.connection.commit()
            return sala_id

    def get_sala(self, id_sala):
        with self.connection.cursor() as cursor:
            query = """
                SELECT idSala, idRegiao, nome, descricao 
                FROM sala
                WHERE idSala = %s;
            """
            cursor.execute(query, (id_sala,))
            result = cursor.fetchone()
            if result:
                return Sala(*result)
            else:
                return None

    def update_sala(self, sala):
        with self.connection.cursor() as cursor:
            query = """
                UPDATE sala
                SET idRegiao = %s, nome = %s, descricao = %s
                WHERE idSala = %s;
            """
            cursor.execute(query, (sala.idRegiao, sala.nome, sala.descricao, sala.idSala))
            self.connection.commit()