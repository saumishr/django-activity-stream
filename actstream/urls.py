from django.conf.urls.defaults import *
from actstream import feeds

urlpatterns = patterns('actstream.views',
    # Syndication Feeds
    url(r'^feed/(?P<content_type_id>\d+)/(?P<object_id>\d+)/atom/$',
        feeds.AtomObjectActivityFeed(), name='actstream_object_feed_atom'),
    url(r'^feed/(?P<content_type_id>\d+)/(?P<object_id>\d+)/$',
        feeds.ObjectActivityFeed(), name='actstream_object_feed'),
    url(r'^feed/(?P<content_type_id>\d+)/atom/$',
        feeds.AtomModelActivityFeed(), name='actstream_model_feed_atom'),
    url(r'^feed/(?P<content_type_id>\d+)/(?P<object_id>\d+)/as/$',
        feeds.ActivityStreamsObjectActivityFeed(),
        name='actstream_object_feed_as'),
    url(r'^feed/(?P<content_type_id>\d+)/$',
        feeds.ModelActivityFeed(), name='actstream_model_feed'),
    url(r'^feed/$', feeds.UserActivityFeed(), name='actstream_feed'),
    url(r'^feed/atom/$', feeds.AtomUserActivityFeed(),
        name='actstream_feed_atom'),

    # Follow/Unfollow API
    url(r'^follow/(?P<content_type_id>\d+)/(?P<object_id>\d+)/$',
        'follow_unfollow', name='actstream_follow'),
    url(r'^follow_all/(?P<content_type_id>\d+)/(?P<object_id>\d+)/$',
        'follow_unfollow', {'actor_only': False}, name='actstream_follow_all'),
    url(r'^unfollow/(?P<content_type_id>\d+)/(?P<object_id>\d+)/$',
        'follow_unfollow', {'do_follow': False}, name='actstream_unfollow'),

    # Follower and Actor lists
    url(r'^followers/(?P<content_type_id>\d+)/(?P<object_id>\d+)/$',
        'followers', name='actstream_followers'),
    url(r'^actors/(?P<content_type_id>\d+)/(?P<object_id>\d+)/$',
        'actor', name='actstream_actor'),
    url(r'^actstream_actor_subset/(?P<content_type_id>\d+)/(?P<object_id>\d+)/(?P<sIndex>\d+)/(?P<lIndex>\d+)/$',
        'actstream_actor_subset', name='actstream_actor_subset'),
    url(r'^actstream_following/(?P<content_type_id>\d+)/(?P<object_id>\d+)/$',
        'actstream_following', name='actstream_following'),
    url(r'^actstream_following_subset/(?P<content_type_id>\d+)/(?P<object_id>\d+)/(?P<sIndex>\d+)/(?P<lIndex>\d+)/$',
        'actstream_following_subset', name='actstream_following_subset'),
    url(r'^actstream_rebuild_cache/(?P<content_type_id>\d+)/(?P<object_id>\d+)/$',
        'actstream_rebuild_cache', name='actstream_rebuild_cache'),
    url(r'^actstream_actor_rebuild_cache/(?P<content_type_id>\d+)/(?P<object_id>\d+)/$',
        'actstream_actor_rebuild_cache', name='actstream_actor_rebuild_cache'),    
    url(r'^actstream_update_activity/(?P<content_type_id>\d+)/(?P<object_id>\d+)/$',
        'actstream_update_activity', name='actstream_update_activity'),

    url(r'^actors/(?P<content_type_id>\d+)/$',
        'model', name='actstream_model'),

    url(r'^detail/(?P<action_id>\d+)/$', 'detail', name='actstream_detail'),
    url(r'^(?P<username>[-\w]+)/$', 'user', name='actstream_user'),
    url(r'^shareAction/(?P<action_id>\d+)/$', 'shareAction', name='shareAction'),
    url(r'^$', 'stream', name='actstream'),
)
