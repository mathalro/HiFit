SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`ClassificacaoPessoa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ClassificacaoPessoa` (
  `idClassificacaoPessoa` INT NOT NULL,
  `somaNota` INT NULL,
  `somaPessoas` INT NULL,
  `total` DOUBLE NULL,
  PRIMARY KEY (`idClassificacaoPessoa`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Profissao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Profissao` (
  `idProfissao` INT NOT NULL,
  `nome` VARCHAR(45) NULL,
  PRIMARY KEY (`idProfissao`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Usuario` (
  `login` VARCHAR(45) NOT NULL,
  `tipoUsuario` TINYINT(1) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `dataNascimento` DATE NOT NULL,
  `telefone` VARCHAR(45) NULL,
  `ClassificacaoPessoa_idClassificacao` INT NOT NULL,
  `cpf` VARCHAR(45) NOT NULL,
  `identificacao` VARCHAR(45) NULL,
  `Profissao_idProfissao1` INT NOT NULL,
  PRIMARY KEY (`login`),
  INDEX `fk_Usuario_ClassificacaoPessoa1_idx` (`ClassificacaoPessoa_idClassificacao` ASC),
  INDEX `fk_Usuario_Profissao1_idx` (`Profissao_idProfissao1` ASC),
  CONSTRAINT `fk_Usuario_ClassificacaoPessoa1`
    FOREIGN KEY (`ClassificacaoPessoa_idClassificacao`)
    REFERENCES `mydb`.`ClassificacaoPessoa` (`idClassificacaoPessoa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Usuario_Profissao1`
    FOREIGN KEY (`Profissao_idProfissao1`)
    REFERENCES `mydb`.`Profissao` (`idProfissao`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Atividade`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Atividade` (
  `idAtividade` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idAtividade`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Caracteristica`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Caracteristica` (
  `idCaracteristica` INT NOT NULL,
  `descricao` VARCHAR(45) NOT NULL,
  `valor` DECIMAL NULL,
  PRIMARY KEY (`idCaracteristica`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Regra`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Regra` (
  `idRegra` INT NOT NULL,
  `pontuacao` INT NULL,
  `restricao` INT NULL,
  `beneficios` INT NULL,
  `maleficios` INT NULL,
  `dataCriacao` DATE NULL,
  `Atividade_idAtividade` INT NOT NULL,
  PRIMARY KEY (`idRegra`),
  INDEX `restricao_idx` (`restricao` ASC),
  INDEX `beneficios_idx` (`beneficios` ASC),
  INDEX `maleficios_idx` (`maleficios` ASC),
  INDEX `fk_Regra_Atividade1_idx` (`Atividade_idAtividade` ASC),
  CONSTRAINT `restricao`
    FOREIGN KEY (`restricao`)
    REFERENCES `mydb`.`Caracteristica` (`idCaracteristica`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `beneficios`
    FOREIGN KEY (`beneficios`)
    REFERENCES `mydb`.`Caracteristica` (`idCaracteristica`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `maleficios`
    FOREIGN KEY (`maleficios`)
    REFERENCES `mydb`.`Caracteristica` (`idCaracteristica`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Regra_Atividade1`
    FOREIGN KEY (`Atividade_idAtividade`)
    REFERENCES `mydb`.`Atividade` (`idAtividade`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Preferencia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Preferencia` (
  `Caracteristica_idCaracteristica` INT NOT NULL,
  INDEX `fk_Preferencia_Caracteristica1_idx` (`Caracteristica_idCaracteristica` ASC),
  CONSTRAINT `fk_Preferencia_Caracteristica1`
    FOREIGN KEY (`Caracteristica_idCaracteristica`)
    REFERENCES `mydb`.`Caracteristica` (`idCaracteristica`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Fisica`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Fisica` (
  `Caracteristica_idCaracteristica` INT NOT NULL,
  INDEX `fk_Fisica_Caracteristica1_idx` (`Caracteristica_idCaracteristica` ASC),
  CONSTRAINT `fk_Fisica_Caracteristica1`
    FOREIGN KEY (`Caracteristica_idCaracteristica`)
    REFERENCES `mydb`.`Caracteristica` (`idCaracteristica`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Fisiologica`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Fisiologica` (
  `Caracteristica_idCaracteristica` INT NOT NULL,
  INDEX `fk_Fisiologica_Caracteristica1_idx` (`Caracteristica_idCaracteristica` ASC),
  CONSTRAINT `fk_Fisiologica_Caracteristica1`
    FOREIGN KEY (`Caracteristica_idCaracteristica`)
    REFERENCES `mydb`.`Caracteristica` (`idCaracteristica`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`CaracteristicaAluno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`CaracteristicaAluno` (
  `Caracteristica_idCaracteristica` INT NOT NULL,
  `Usuario_login` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Caracteristica_idCaracteristica`, `Usuario_login`),
  INDEX `fk_Caracteristica_has_Aluno_Caracteristica1_idx` (`Caracteristica_idCaracteristica` ASC),
  INDEX `fk_Caracteristica_has_Aluno_Usuario1_idx` (`Usuario_login` ASC),
  CONSTRAINT `fk_Caracteristica_has_Aluno_Caracteristica1`
    FOREIGN KEY (`Caracteristica_idCaracteristica`)
    REFERENCES `mydb`.`Caracteristica` (`idCaracteristica`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Caracteristica_has_Aluno_Usuario1`
    FOREIGN KEY (`Usuario_login`)
    REFERENCES `mydb`.`Usuario` (`login`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ClassificacaoRecomendacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ClassificacaoRecomendacao` (
  `idClassificacaoRecomendacao` INT NOT NULL,
  `somaNota` INT NULL,
  `somaPessoas` INT NULL,
  `total` DOUBLE NULL,
  PRIMARY KEY (`idClassificacaoRecomendacao`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Recomendacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Recomendacao` (
  `Regra_idRegra` INT NOT NULL,
  `dataRecomendacao` DATE NULL,
  `ClassificacaoRecomendacao_idClassificacaoRecomendacao` INT NOT NULL,
  `Usuario_login` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Regra_idRegra`, `Usuario_login`),
  INDEX `fk_Aluno_has_Regra_Regra1_idx` (`Regra_idRegra` ASC),
  INDEX `fk_Recomendacao_ClassificacaoRecomendacao1_idx` (`ClassificacaoRecomendacao_idClassificacaoRecomendacao` ASC),
  INDEX `fk_Recomendacao_Usuario1_idx` (`Usuario_login` ASC),
  CONSTRAINT `fk_Aluno_has_Regra_Regra1`
    FOREIGN KEY (`Regra_idRegra`)
    REFERENCES `mydb`.`Regra` (`idRegra`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Recomendacao_ClassificacaoRecomendacao1`
    FOREIGN KEY (`ClassificacaoRecomendacao_idClassificacaoRecomendacao`)
    REFERENCES `mydb`.`ClassificacaoRecomendacao` (`idClassificacaoRecomendacao`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Recomendacao_Usuario1`
    FOREIGN KEY (`Usuario_login`)
    REFERENCES `mydb`.`Usuario` (`login`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Denuncia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Denuncia` (
  `idDenuncia` INT NOT NULL,
  `titulo` VARCHAR(45) NOT NULL,
  `conteudo` VARCHAR(45) NOT NULL,
  `data` DATE NOT NULL,
  `Usuario_login` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idDenuncia`),
  INDEX `fk_Denuncia_Usuario1_idx` (`Usuario_login` ASC),
  CONSTRAINT `fk_Denuncia_Usuario1`
    FOREIGN KEY (`Usuario_login`)
    REFERENCES `mydb`.`Usuario` (`login`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ClassificacaoPost`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ClassificacaoPost` (
  `idClassificacaoPost` INT NOT NULL,
  `somaNota` INT NULL,
  `somaPessoas` INT NULL,
  `total` DOUBLE NULL,
  PRIMARY KEY (`idClassificacaoPost`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Post`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Post` (
  `idPost` INT NOT NULL,
  `conteudo` VARCHAR(45) NOT NULL,
  `data` DATE NOT NULL,
  `Usuario_login` VARCHAR(45) NOT NULL,
  `ClassificacaoPost_idClassificacaoPost` INT NOT NULL,
  PRIMARY KEY (`idPost`),
  INDEX `fk_Post_Usuario1_idx` (`Usuario_login` ASC),
  INDEX `fk_Post_ClassificacaoPost1_idx` (`ClassificacaoPost_idClassificacaoPost` ASC),
  CONSTRAINT `fk_Post_Usuario1`
    FOREIGN KEY (`Usuario_login`)
    REFERENCES `mydb`.`Usuario` (`login`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Post_ClassificacaoPost1`
    FOREIGN KEY (`ClassificacaoPost_idClassificacaoPost`)
    REFERENCES `mydb`.`ClassificacaoPost` (`idClassificacaoPost`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Comentario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Comentario` (
  `idComentario` INT NOT NULL,
  `conteudo` VARCHAR(45) NULL,
  `data` DATE NULL,
  `Post_idPost` INT NOT NULL,
  PRIMARY KEY (`idComentario`),
  INDEX `fk_Comentario_Post1_idx` (`Post_idPost` ASC),
  CONSTRAINT `fk_Comentario_Post1`
    FOREIGN KEY (`Post_idPost`)
    REFERENCES `mydb`.`Post` (`idPost`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`FeedbackSistema`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`FeedbackSistema` (
  `idFeedback` INT NOT NULL,
  `somaNota` INT NULL,
  `somaPessoas` INT NULL,
  `total` DOUBLE NULL,
  PRIMARY KEY (`idFeedback`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Mensagem`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Mensagem` (
  `idMensagem` INT NOT NULL,
  `conteudo` VARCHAR(45) NULL,
  `data` DATE NULL,
  `Usuario_login` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idMensagem`),
  INDEX `fk_Mensagem_Usuario1_idx` (`Usuario_login` ASC),
  CONSTRAINT `fk_Mensagem_Usuario1`
    FOREIGN KEY (`Usuario_login`)
    REFERENCES `mydb`.`Usuario` (`login`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Sugestao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Sugestao` (
  `idSugestao` INT NOT NULL,
  `conteudo` VARCHAR(45) NULL,
  `data` DATE NULL,
  PRIMARY KEY (`idSugestao`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
