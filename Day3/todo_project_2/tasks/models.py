from functools import total_ordering
from django.db import models
from django.utils.translation import TranslatorCommentWarning

# Create your models here.
# ORM - Object Relational Mapper
# takes your python objects, and stores them as db tables and rows

# Models for tables

# model, view, controller are decoupled

# LLD requirements
# - user can add tasks
# - a task can be tagged with one or more tags
# - can search for tasks by content or by tag
# - tasks can have an urgency and an importance
# - tasks can have a status - pending, completed, dropped

# Detect nouns -> usually become entities/models
# Detect attributes and relationships


class Tag(models.Model):
    name = models.CharField(max_length=255)

# Create an rich API for us for free

class Task(models.Model):   # class => table
    content = models.TextField()    # field => column in the table
    deadline = models.DateTimeField()
    created_at = models.DateTimeField()
    completed_at = models.DateTimeField()
    tags = models.ManyToManyField(Tag)   # got additional table because of many-to-many relation

    class TaskStatus(models.TextChoices): # enumeration
        COMPLETED = "CO", "Completed"
        PENDING = "PE", "Pending"
        DROPPED = "DR", "Dropped"

    status = models.CharField(
        choices = TaskStatus.choices,
        default = TaskStatus.PENDING,
        max_length = 2,
    )   #  must have restricted set of choices

# Whenever I change my DB schema
# - My old DB is now useless
# - create a new DB?
# - somehow reenter the data in the new DB  --> is a hefty task
# I don't want the users to re-enter the data

# Migration - Migrate the previous data to new DB

# Approach-1: delete DB, create new DB, enter data myself
# Approach-2: write a script that looks at the prev DB, 
#             and copies the data to the new DB
# Whenever I change my schema, I have to write this script again and again
# I have the previous DB schema
# I ahve the current models in Django

# Can I write a script that automatically find the differences 
# and writes the migration script for me?
# Django provides this out of the box


# 1 task can have 1 or more tags
# 1 tag (like shopping) can also have multiple tasks
# Many to Many Relationship


# OneToOne Relationship => column in your tables
# OneToMany Relationship => column in your tables
# ManyToOne Relationship => column in your tables
# ManyToMany Relationship => crete other table


# task_Tags => 
# id  |  task_id (F.K of tasak table) | tag_id (F.K of tag table) |




    
    
    

