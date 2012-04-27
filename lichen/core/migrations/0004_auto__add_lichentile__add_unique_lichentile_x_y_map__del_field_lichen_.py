# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
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

        # Deleting field 'Lichen.diameter'
        db.delete_column('core_lichen', 'diameter')

        # Deleting field 'Lichen.map'
        db.delete_column('core_lichen', 'map_id')

        # Deleting field 'Lichen.y'
        db.delete_column('core_lichen', 'y')

        # Deleting field 'Lichen.x'
        db.delete_column('core_lichen', 'x')

        # Adding field 'Lichen.z_speed'
        db.add_column('core_lichen', 'z_speed',
                      self.gf('django.db.models.fields.FloatField')(default=0.1),
                      keep_default=False)

        # Adding field 'Lichen.max_tiles'
        db.add_column('core_lichen', 'max_tiles',
                      self.gf('django.db.models.fields.IntegerField')(default=5),
                      keep_default=False)

    def backwards(self, orm):
        # Removing unique constraint on 'LichenTile', fields ['x', 'y', 'map']
        db.delete_unique('core_lichentile', ['x', 'y', 'map_id'])

        # Deleting model 'LichenTile'
        db.delete_table('core_lichentile')

        # Adding field 'Lichen.diameter'
        db.add_column('core_lichen', 'diameter',
                      self.gf('django.db.models.fields.IntegerField')(default=3),
                      keep_default=False)

        # Adding field 'Lichen.map'
        db.add_column('core_lichen', 'map',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['core.Map']),
                      keep_default=False)

        # Adding field 'Lichen.y'
        db.add_column('core_lichen', 'y',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Lichen.x'
        db.add_column('core_lichen', 'x',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Lichen.z_speed'
        db.delete_column('core_lichen', 'z_speed')

        # Deleting field 'Lichen.max_tiles'
        db.delete_column('core_lichen', 'max_tiles')

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
            'z_speed': ('django.db.models.fields.FloatField', [], {'default': '0.1'})
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