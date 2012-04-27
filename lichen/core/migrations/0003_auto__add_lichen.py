# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Lichen'
        db.create_table('core_lichen', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('x', self.gf('django.db.models.fields.IntegerField')()),
            ('y', self.gf('django.db.models.fields.IntegerField')()),
            ('map', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Map'])),
            ('diameter', self.gf('django.db.models.fields.IntegerField')(default=3)),
        ))
        db.send_create_signal('core', ['Lichen'])

    def backwards(self, orm):
        # Deleting model 'Lichen'
        db.delete_table('core_lichen')

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
            'diameter': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
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