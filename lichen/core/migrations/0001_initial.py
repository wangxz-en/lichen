# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Map'
        db.create_table('core_map', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')()),
            ('height', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('core', ['Map'])

        # Adding model 'Cell'
        db.create_table('core_cell', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('x', self.gf('django.db.models.fields.IntegerField')()),
            ('y', self.gf('django.db.models.fields.IntegerField')()),
            ('map', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Map'])),
        ))
        db.send_create_signal('core', ['Cell'])

        # Adding model 'Wall'
        db.create_table('core_wall', (
            ('cell_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Cell'], unique=True, primary_key=True)),
            ('destructible', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['Wall'])

        # Adding model 'Unit'
        db.create_table('core_unit', (
            ('cell_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Cell'], unique=True, primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('core', ['Unit'])

    def backwards(self, orm):
        # Deleting model 'Map'
        db.delete_table('core_map')

        # Deleting model 'Cell'
        db.delete_table('core_cell')

        # Deleting model 'Wall'
        db.delete_table('core_wall')

        # Deleting model 'Unit'
        db.delete_table('core_unit')

    models = {
        'core.cell': {
            'Meta': {'object_name': 'Cell'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Map']"}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'y': ('django.db.models.fields.IntegerField', [], {})
        },
        'core.map': {
            'Meta': {'object_name': 'Map'},
            'height': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        },
        'core.unit': {
            'Meta': {'object_name': 'Unit', '_ormbases': ['core.Cell']},
            'cell_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Cell']", 'unique': 'True', 'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'core.wall': {
            'Meta': {'object_name': 'Wall', '_ormbases': ['core.Cell']},
            'cell_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Cell']", 'unique': 'True', 'primary_key': 'True'}),
            'destructible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['core']