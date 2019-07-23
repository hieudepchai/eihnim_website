# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    # Field name made lowercase.
    accountid = models.AutoField(db_column='AccountID', primary_key=True)
    # Field name made lowercase.
    username = models.CharField(
        db_column='Username', unique=True, max_length=255)
    # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255)
    # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255)
    # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255)
    # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=255)
    # Field name made lowercase.
    phone = models.CharField(db_column='Phone', unique=True, max_length=11)
    # Field name made lowercase.
    accounttypeid = models.ForeignKey(
        'Accounttype', models.DO_NOTHING, db_column='AccountTypeID')
    # Field name made lowercase.
    profilepicture = models.CharField(
        db_column='ProfilePicture', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    valid = models.IntegerField(db_column='Valid', blank=True, null=True)
    # Field name made lowercase.
    datecreated = models.DateTimeField(
        db_column='DateCreated', blank=True, null=True)
    # Field name made lowercase.
    lastmodified = models.DateTimeField(
        db_column='LastModified', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Account'


class Accounttype(models.Model):
    # Field name made lowercase.
    accounttypeid = models.AutoField(
        db_column='AccountTypeID', primary_key=True)
    # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=255)
    # Field name made lowercase.
    readerright = models.IntegerField(
        db_column='ReaderRight', blank=True, null=True)
    # Field name made lowercase.
    journalistright = models.IntegerField(
        db_column='JournalistRight', blank=True, null=True)
    # Field name made lowercase.
    adminright = models.IntegerField(
        db_column='AdminRight', blank=True, null=True)
    # Field name made lowercase.
    accountmng = models.IntegerField(
        db_column='AccountMng', blank=True, null=True)
    # Field name made lowercase.
    accounttypemng = models.IntegerField(
        db_column='AccountTypeMng', blank=True, null=True)
    # Field name made lowercase.
    articlemng = models.IntegerField(
        db_column='ArticleMng', blank=True, null=True)
    # Field name made lowercase.
    commentmng = models.IntegerField(
        db_column='CommentMng', blank=True, null=True)
    # Field name made lowercase.
    bookmarkmng = models.IntegerField(
        db_column='BookmarkMng', blank=True, null=True)
    # Field name made lowercase.
    feedbackmng = models.IntegerField(
        db_column='FeedbackMng', blank=True, null=True)
    # Field name made lowercase.
    imagemng = models.IntegerField(db_column='ImageMng', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AccountType'


class Article(models.Model):
    # Field name made lowercase.
    articleid = models.AutoField(db_column='ArticleID', primary_key=True)
    # Field name made lowercase.
    heading = models.CharField(db_column='Heading', max_length=255)
    # Field name made lowercase.
    shortdescription = models.TextField(
        db_column='ShortDescription', blank=True, null=True)
    # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)
    # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryID')
    # Field name made lowercase.
    subcategoryid = models.IntegerField(
        db_column='SubCategoryID', blank=True, null=True)
    # Field name made lowercase.
    journalistid = models.ForeignKey(
        Account, models.DO_NOTHING, db_column='JournalistID')
    # Field name made lowercase.
    censored = models.IntegerField(db_column='Censored', blank=True, null=True)
    # Field name made lowercase.
    draft = models.IntegerField(db_column='Draft', blank=True, null=True)
    # Field name made lowercase.
    trash = models.IntegerField(db_column='Trash', blank=True, null=True)
    # Field name made lowercase.
    datecreated = models.DateTimeField(
        db_column='DateCreated', blank=True, null=True)
    # Field name made lowercase.
    lastmodified = models.DateTimeField(
        db_column='LastModified', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Article'


class Bookmark(models.Model):
    # Field name made lowercase.
    bookmarkid = models.AutoField(db_column='BookmarkID', primary_key=True)
    # Field name made lowercase.
    accountid = models.ForeignKey(
        Account, models.DO_NOTHING, db_column='AccountID')
    # Field name made lowercase.
    articleid = models.ForeignKey(
        Article, models.DO_NOTHING, db_column='ArticleID')
    # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255)
    # Field name made lowercase.
    datecreated = models.DateTimeField(
        db_column='DateCreated', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Bookmark'
        unique_together = (('bookmarkid', 'accountid'),)


class Category(models.Model):
    # Field name made lowercase.
    categoryid = models.AutoField(db_column='CategoryID', primary_key=True)
    # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)
    # Field name made lowercase.
    parentcategoryid = models.ForeignKey(
        'self', models.DO_NOTHING, db_column='ParentCategoryID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Category'


class Comment(models.Model):
    # Field name made lowercase.
    commentid = models.AutoField(db_column='CommentID', primary_key=True)
    # Field name made lowercase.
    articleid = models.ForeignKey(
        Article, models.DO_NOTHING, db_column='ArticleID')
    # Field name made lowercase.
    repliedcommentid = models.IntegerField(
        db_column='RepliedCommentID', blank=True, null=True)
    # Field name made lowercase.
    accountid = models.ForeignKey(
        Account, models.DO_NOTHING, db_column='AccountID')
    # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)
    # Field name made lowercase.
    nooflikes = models.IntegerField(
        db_column='NoOfLikes', blank=True, null=True)
    # Field name made lowercase.
    level = models.IntegerField(db_column='Level')
    # Field name made lowercase.
    datecreated = models.DateTimeField(
        db_column='DateCreated', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Comment'
        unique_together = (('commentid', 'articleid'),)


class Image(models.Model):
    # Field name made lowercase.
    imageid = models.AutoField(db_column='ImageID', primary_key=True)
    # Field name made lowercase.
    source = models.CharField(
        db_column='Source', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    articleid = models.ForeignKey(
        Article, models.DO_NOTHING, db_column='ArticleID', blank=True, null=True)
    # Field name made lowercase.
    accountid = models.ForeignKey(
        Account, models.DO_NOTHING, db_column='AccountID', blank=True, null=True)
    # Field name made lowercase.
    datecreated = models.DateTimeField(
        db_column='DateCreated', blank=True, null=True)
    # Field name made lowercase.
    thumbnail = models.IntegerField(
        db_column='Thumbnail', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Image'


class Message(models.Model):
    # Field name made lowercase.
    messageid = models.AutoField(db_column='MessageID', primary_key=True)
    # Field name made lowercase.
    articleid = models.ForeignKey(
        Article, models.DO_NOTHING, db_column='ArticleID')
    # Field name made lowercase.
    senderid = models.ForeignKey(
        Account, models.DO_NOTHING, db_column='SenderID', related_name='SenderID')
    receiverid = models.ForeignKey(Account, models.DO_NOTHING, db_column='ReceiverID',
                                   blank=True, null=True, related_name='ReceiverID')  # Field name made lowercase.
    # Field name made lowercase.
    repliedmessageid = models.ForeignKey(
        'self', models.DO_NOTHING, db_column='RepliedMessageID', blank=True, null=True)
    # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)
    # Field name made lowercase.
    datecreated = models.DateTimeField(
        db_column='DateCreated', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Message'


class Updatearticleactivity(models.Model):
    # Field name made lowercase.
    actionid = models.AutoField(db_column='ActionID', primary_key=True)
    # Field name made lowercase.
    doerid = models.ForeignKey(Account, models.DO_NOTHING, db_column='DoerID')
    # Field name made lowercase.
    articleid = models.ForeignKey(
        Article, models.DO_NOTHING, db_column='ArticleID')
    # Field name made lowercase.
    censored = models.IntegerField(db_column='Censored', blank=True, null=True)
    # Field name made lowercase.
    draft = models.IntegerField(db_column='Draft', blank=True, null=True)
    # Field name made lowercase.
    trash = models.IntegerField(db_column='Trash', blank=True, null=True)
    # Field name made lowercase.
    created = models.IntegerField(db_column='Created', blank=True, null=True)
    # Field name made lowercase.
    datecreated = models.DateTimeField(
        db_column='DateCreated', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UpdateArticleActivity'
