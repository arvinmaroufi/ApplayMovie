let player = new Plyr('video', {
    controls:
        ['play-large', 'play', 'progress',
            'current-time', 'mute', 'volume', 'captions', 'settings', 'fullscreen'],
    tooltips: {
        controls: true,
    },
});