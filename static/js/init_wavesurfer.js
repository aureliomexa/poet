function createWaveSurferElement(containerId, audioFilepath, waveformPeaks) {

    const peaksId = containerId + "-peaks";
    const timeRemainingId = containerId + "-time-remaining";
    const timeCurrentId = containerId + "-time-current";
    const timeTotalId = containerId + "-time-total";


    const rootElement = document.getElementById(containerId);

    const waveFormDiv = document.createElement("div");
    rootElement.appendChild(waveFormDiv);

    waveFormDiv.classList.add("row");
    const innerWaveFormDiv = document.createElement("div");
    waveFormDiv.appendChild(innerWaveFormDiv);
    innerWaveFormDiv.id = peaksId;

    const wavesurfer = WaveSurfer.create({
        // Use the id or class-name of the element you created, as a selector
        container: "#" + peaksId,
        backend: "MediaElement",
        // The color can be either a simple CSS color or a Canvas gradient
        waveColor: "grey",
        progressColor: "black",
        cursorColor: "grey",
        // This parameter makes the waveform look like SoundCloud"s player
        barWidth: 2,
        normalize: true
    });

    if (waveformPeaks != null) {
        wavesurfer.load(audioFilepath, waveformPeaks);
    } else {
        wavesurfer.load(audioFilepath);
    }

    const buttonsDiv = document.createElement("div");
    rootElement.appendChild(buttonsDiv);
    buttonsDiv.classList.add("row");
    const playDiv = document.createElement("div");

    buttonsDiv.appendChild(playDiv);
    playDiv.classList.add('col-md-2');
    playDiv.classList.add('text-center');

    const playButton = document.createElement("button");
    playDiv.appendChild(playButton);

    playButton.innerHTML = "&#9658";
    playButton.onclick = function() { wavesurfer.playPause(); };

    const volumeDiv = document.createElement("div");
    buttonsDiv.appendChild(volumeDiv);

    volumeDiv.classList.add('col-md-6');

    const volumeSlider = document.createElement('input');
    volumeDiv.appendChild(volumeSlider);
    volumeSlider.type = "range";
    volumeSlider.max = "0";
    volumeSlider.max = "1";
    volumeSlider.step = "0.01";

    const timeDiv = document.createElement('div'),
        remainingSpan = document.createElement('span'),
        currentSpan = document.createElement('span'),
        totalSpan = document.createElement('span');

    timeDiv.classList.add('col-md-4');
    timeDiv.classList.add('text-left');
    const spanClass = 'time-span';
    totalSpan.classList.add(spanClass);
    currentSpan.classList.add(spanClass);
    remainingSpan.classList.add(spanClass);

    remainingSpan.id = timeRemainingId;
    currentSpan.id = timeCurrentId;
    totalSpan.id = timeTotalId;

    buttonsDiv.appendChild(timeDiv);
    timeDiv.appendChild(remainingSpan);
    timeDiv.appendChild(currentSpan);
    timeDiv.appendChild(totalSpan);


    wavesurfer.on('ready', function () {

        wavesurfer.setVolume(0.5);

        volumeSlider.value = wavesurfer.backend.getVolume();

        const totalTime = wavesurfer.getDuration();
        const currentTime = Math.round(wavesurfer.getCurrentTime());
        const remainingTime = Math.round(totalTime - currentTime);

        document.getElementById(timeCurrentId).innerText = currentTime;
        document.getElementById(timeTotalId).innerText = Math.round(totalTime);
        document.getElementById(timeRemainingId).innerText = remainingTime;

        const onChangeVolume = function (e) {
            wavesurfer.setVolume(e.target.value);
        };

        volumeSlider.addEventListener('input', onChangeVolume);
        volumeSlider.addEventListener('change', onChangeVolume);

    });

    wavesurfer.on('audioprocess', function() {
        if(wavesurfer.isPlaying()) {
            const totalTime = wavesurfer.getDuration();
            const currentTime = Math.round(wavesurfer.getCurrentTime());
            const remainingTime = Math.round(totalTime - currentTime);


            document.getElementById(timeCurrentId).innerText = currentTime;
            document.getElementById(timeTotalId).innerText = Math.round(totalTime);
            document.getElementById(timeRemainingId).innerText = remainingTime;
        }
    });
}

if (typeof audioIterator !== 'undefined') {
     for (let i = 0; i < audioIterator.waveformPeaks.length; i++) {
        createWaveSurferElement(
            audioIterator.containersIds[i],
            audioIterator.audioPaths[i],
            audioIterator.waveformPeaks[i]);
    }
}




