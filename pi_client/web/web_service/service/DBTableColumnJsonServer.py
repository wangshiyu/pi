# encoding: utf-8
# !/usr/bin/python3
from pi_db.common.dao.DirectiveInfoDao import DirectiveInfoDao
from pi_db.common.entity.DirectiveInfoEntity import DirectiveInfoEntity
from pi_db.common.dao.DirectiveCommadAlgorithmDao import DirectiveCommadAlgorithmDao
from pi_db.common.entity.DirectiveCommadAlgorithmEntity import DirectiveCommadAlgorithmEntity
from pi_db.common.dao.DirectiveHardwareDao import DirectiveHardwareDao
from pi_db.common.entity.DirectiveHardwareEntity import DirectiveHardwareEntity
from pi_db.common.dao.DirectiveRequestParameterMappingDao import DirectiveRequestParameterMappingDao
from pi_db.common.entity.DirectiveRequestParameterMappingEntity import DirectiveRequestParameterMappingEntity
from pi_db.common.dao.TrggerInfoDao import TrggerInfoDao
from pi_db.common.entity.TrggerInfoEntity import TrggerInfoEntity
from pi_common.constant.TableConstant import TableConstant, ColumnConstant

"""数据库表字段JSON数据服务"""


class DBTableColumnJsonServer:
    directiveInfoDao = DirectiveInfoDao()
    directiveCommadAlgorithmDao = DirectiveCommadAlgorithmDao()
    directiveHardwareDao = DirectiveHardwareDao()
    directiveRequestParameterMappingDao = DirectiveRequestParameterMappingDao()
    trggerInfoDao = TrggerInfoDao()

    """
    获取json字符串
    """

    def getJsonStr(self, type, id, column):
        if TableConstant.TB_DIRECTIVE_INFO == type:
            directiveInfoEntity = self.directiveInfoDao.getById(id)
            if ColumnConstant.METHOD_JSON == column:
                return directiveInfoEntity.methodJson
            elif ColumnConstant.IMPORT_CODE_JSON == column:
                return directiveInfoEntity.importCodeJson
            else:
                pass

        elif TableConstant.TB_DIRECTIVE_COMMAD_ALGORITHM == type:
            directiveCommadAlgorithmEntity = self.directiveCommadAlgorithmDao.getById(id)
            if ColumnConstant.INPUT_PARAMETER_TYPE_JSON == column:
                return directiveCommadAlgorithmEntity.input_parameter_type_json
            else:
                pass
        elif TableConstant.TB_DIRECTIVE_HARDWARE == type:
            directiveHardwareEntity = self.directiveHardwareDao.getById(id)
            if ColumnConstant.CHANNEL_JSON == column:
                return directiveHardwareEntity.channelJson
            elif ColumnConstant.EXECUTE_JSON == column:
                return directiveHardwareEntity.executeJson
            elif ColumnConstant.DIRECTIVE_COMMAD_ALGORITHM_JSON == column:
                return directiveHardwareEntity.directiveCommadAlgorithmJson
            else:
                pass
        elif TableConstant.TB_DIRECTIVE_REQUEST_PARAMETER_MAPPING == type:
            if ColumnConstant.PARAMETERS_MAPPING_JSON == column:
                pass
            else:
                pass
        elif TableConstant.TB_TRGGER_INFO == type:
            if ColumnConstant.TRIGGER_TASK_JSON == column:
                pass
            else:
                pass
        else:
            pass

    """
    更新json字符串
    """

    def updateJsonStr(self, type, id, column, jsonStr):
        if TableConstant.TB_DIRECTIVE_INFO == type:
            if ColumnConstant.METHOD_JSON == column:
                pass
            elif ColumnConstant.IMPORT_CODE_JSON == column:
                pass
            elif ColumnConstant.INIT_CODE == column:
                pass
            elif ColumnConstant.OTHER_CODE == column:
                pass
            else:
                pass

        elif TableConstant.TB_DIRECTIVE_COMMAD_ALGORITHM == type:
            if ColumnConstant.INPUT_PARAMETER_TYPE_JSON == column:
                pass
            else:
                pass
        elif TableConstant.TB_DIRECTIVE_HARDWARE == type:
            if ColumnConstant.CHANNEL_JSON == column:
                pass
            elif ColumnConstant.EXECUTE_JSON == column:
                pass
            elif ColumnConstant.DIRECTIVE_COMMAD_ALGORITHM_JSON == column:
                pass
            else:
                pass
        elif TableConstant.TB_DIRECTIVE_REQUEST_PARAMETER_MAPPING == type:
            if ColumnConstant.PARAMETERS_MAPPING_JSON == column:
                pass
            else:
                pass
        elif TableConstant.TB_TRGGER_INFO == type:
            if ColumnConstant.TRIGGER_TASK_JSON == column:
                pass
            else:
                pass
        else:
            pass

    """
    校验json字符串
    """

    def checkJsonStr(self, jsonStr):
        pass
