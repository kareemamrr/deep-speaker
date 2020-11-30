navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => { handlerFunction(stream) })

function handlerFunction(stream) {
    rec = new MediaRecorder(stream);
    rec.ondataavailable = e => {
        audioChunks.push(e.data);
        if (rec.state == "inactive") {
            let blob = new Blob(audioChunks, { type: 'audio/mpeg-3' });
            recordedAudio.src = URL.createObjectURL(blob);
            recordedAudio.controls = true;
            recordedAudio.autoplay = false;
            sendData(blob)
        }
    }
}

async function sendData(file) {
    formData = new FormData();
    // formData.append('uploadedfile', file);
    formData.append('username', 'Kareem');
    const response = await fetch('http://localhost:8000/test', {
        method: 'POST',
        data: formData
    })
}

record.onclick = e => {
    console.log('Record clicked')
    record.disabled = true;
    stopRecord.disabled = false;
    audioChunks = [];
    rec.start();
}


stopRecord.onclick = e => {
    console.log('Stop clicked')
    stopRecord.disabled = true;
    record.disabled = false;
    rec.stop();
}