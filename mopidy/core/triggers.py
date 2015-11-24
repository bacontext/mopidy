import logging
from mopidy.core import listener

logger = logging.getLogger(__name__)


def trigger_track_playback_paused(time_position, tl_track, current_track):
    logger.debug('Triggering track playback paused event')
    if current_track is None:
        return
    listener.CoreListener.send(
        'track_playback_paused',
        tl_track=tl_track,
        time_position=time_position)

def trigger_track_playback_resumed(time_position, tl_track, current_track):
    logger.debug('Triggering track playback resumed event')
    if current_track is None:
        return
    listener.CoreListener.send(
        'track_playback_resumed',
        tl_track=tl_track,
        time_position=time_position)

def trigger_track_playback_started(core, tl_track):
    if tl_track is None:
        return

    logger.debug('Triggering track playback started event')
    core.tracklist._mark_playing(tl_track)
    core.history._add_track(tl_track.track)
    listener.CoreListener.send('track_playback_started', tl_track=tl_track)

def trigger_track_playback_ended(core, time_position_before_stop, tl_track, previous):
    if tl_track is None:
        return

    logger.debug('Triggering track playback ended event')

    if not previous:
        core.tracklist._mark_played(tl_track)

    # TODO: Use the lowest of track duration and position.
    listener.CoreListener.send(
        'track_playback_ended',
        tl_track=tl_track,
        time_position=time_position_before_stop)

def trigger_playback_state_changed(old_state, new_state):
    logger.debug('Triggering playback state change event')
    listener.CoreListener.send(
        'playback_state_changed',
        old_state=old_state, new_state=new_state)

def trigger_seeked(time_position):
    # TODO: Trigger this from audio events?
    logger.debug('Triggering seeked event')
    listener.CoreListener.send('seeked', time_position=time_position)
