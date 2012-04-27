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
            ('width', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=100)),
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

        # Adding unique constraint on 'Cell', fields ['x', 'y', 'map']
        db.create_unique('core_cell', ['x', 'y', 'map_id'])

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

        # Adding model 'Lichen'
        db.create_table('core_lichen', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('x_speed', self.gf('django.db.models.fields.FloatField')(default=-1)),
            ('y_speed', self.gf('django.db.models.fields.FloatField')(default=None)),
            ('z_speed', self.gf('django.db.models.fields.FloatField')(default=None)),
            ('max_tiles', self.gf('django.db.models.fields.IntegerField')(default=5)),
        ))
        db.send_create_signal('core', ['Lichen'])

        # Adding model 'LichenTile'
        db.create_table('core_lichentile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('x', self.gf('django.db.models.fields.IntegerField')()),
            ('y', self.gf('django.db.models.fields.IntegerField')()),
            ('map', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Map'])),
            ('lichen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Lichen'])),
        ))
        db.send_create_signal('core', ['LichenTile'])

        # Adding unique constraint on 'LichenTile', fields ['x', 'y', 'map']
        db.create_unique('core_lichentile', ['x', 'y', 'map_id'])

    def backwards(self, orm):
        # Removing unique constraint on 'LichenTile', fields ['x', 'y', 'map']
        db.delete_unique('core_lichentile', ['x', 'y', 'map_id'])

        # Removing unique constraint on 'Cell', fields ['x', 'y', 'map']
        db.delete_unique('core_cell', ['x', 'y', 'map_id'])

        # Deleting model 'Map'
        db.delete_table('core_map')

        # Deleting model 'Cell'
        db.delete_table('core_cell')

        # Deleting model 'Wall'
        db.delete_table('core_wall')

        # Deleting model 'Unit'
        db.delete_table('core_unit')

        # Deleting model 'Lichen'
        db.delete_table('core_lichen')

        # Deleting model 'LichenTile'
        db.delete_table('core_lichentile')

    models = {
        'core.cell': {
            'Meta': {'unique_together': "(('x', 'y', 'map'),)", 'object_name': 'Cell'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Map']"}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'y': ('django.db.models.fields.IntegerField', [], {})
        },
        'core.lichen': {
            'Meta': {'object_name': 'Lichen'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_tiles': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'x_speed': ('django.db.models.fields.FloatField', [], {'default': '1'}),
            'y_speed': ('django.db.models.fields.FloatField', [], {'default': 'None'}),
            'z_speed': ('django.db.models.fields.FloatField', [], {'default': 'None'})
        },
        'core.lichentile': {
            'Meta': {'unique_together': "(('x', 'y', 'map'),)", 'object_name': 'LichenTile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lichen': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Lichen']"}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Map']"}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'y': ('django.db.models.fields.IntegerField', [], {})
        },
        'core.map': {
            'Meta': {'object_name': 'Map'},
            'height': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '100'})
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