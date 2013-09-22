# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Survey'
        db.create_table(u'brinder_survey', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'brinder', ['Survey'])

        # Adding model 'Question'
        db.create_table(u'brinder_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brinder.Survey'])),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'brinder', ['Question'])

        # Adding model 'FacebookId'
        db.create_table(u'brinder_facebookid', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('facebook_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'brinder', ['FacebookId'])

        # Adding model 'Message'
        db.create_table(u'brinder_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sender', to=orm['auth.User'])),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(related_name='recipient', to=orm['auth.User'])),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brinder.Survey'])),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'brinder', ['Message'])

        # Adding model 'Answer'
        db.create_table(u'brinder_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brinder.Question'])),
            ('message', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brinder.Message'])),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'brinder', ['Answer'])


    def backwards(self, orm):
        # Deleting model 'Survey'
        db.delete_table(u'brinder_survey')

        # Deleting model 'Question'
        db.delete_table(u'brinder_question')

        # Deleting model 'FacebookId'
        db.delete_table(u'brinder_facebookid')

        # Deleting model 'Message'
        db.delete_table(u'brinder_message')

        # Deleting model 'Answer'
        db.delete_table(u'brinder_answer')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'brinder.answer': {
            'Meta': {'object_name': 'Answer'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['brinder.Message']"}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['brinder.Question']"}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'brinder.facebookid': {
            'Meta': {'object_name': 'FacebookId'},
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'brinder.message': {
            'Meta': {'object_name': 'Message'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recipient'", 'to': u"orm['auth.User']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sender'", 'to': u"orm['auth.User']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['brinder.Survey']"})
        },
        u'brinder.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['brinder.Survey']"})
        },
        u'brinder.survey': {
            'Meta': {'object_name': 'Survey'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['brinder']