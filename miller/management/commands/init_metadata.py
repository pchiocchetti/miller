#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging, json

from miller.models import Story

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

logger = logging.getLogger('miller.commands')


class Command(BaseCommand):
  help = 'Initialize the JSON field metadata for Story instances'

  def add_arguments(self, parser):
    pass

  def handle(self, *args, **options):
    
    stories = Story.objects.all()

    # The `iterator()` method ensures only a few rows are fetched from
    # the database at a time, saving memory.
    for story in stories.iterator():
      logger.debug('reconcile metadata of story id: %s' % story.id)
      story.save()
    
    logger.debug('command finished.')
      

