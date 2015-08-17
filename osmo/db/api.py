# -*- coding: utf-8 -*-
#
#   Refrence
#       -  oslo.db
#
#   Library
#       - sqlalchemy
#
#   Usage
#       - neutron/neutron/db/api.py
#

from oslo.config import cfg
from oslo_db.sqlalchemy import session

_FACADE = None


def _create_facade_lazily():
    global _FACADE
    if _FACADE is None:
        _FACADE = session.EngineFacade.from_config(cfg.CONF)
    return _FACADE


def get_engine():
    facade = _create_facade_lazily()
    return facade.get_engine()


def get_session(**kwargs):
    # See: http://docs.sqlalchemy.org/en/rel_0_9/orm/session.html
    #      #unitofwork-contextual
    facade = _create_facade_lazily()
    db_session = facade.get_session(**kwargs)
    return db_session