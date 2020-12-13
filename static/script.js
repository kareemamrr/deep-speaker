navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => { handlerFunction(stream) })
var blob;

function handlerFunction(stream) {
    rec = new MediaRecorder(stream);
    rec.ondataavailable = e => {
        audioChunks.push(e.data);
        if (rec.state == "inactive") {
            blob = new Blob(audioChunks, { type: 'audio/wav' });
            recordedAudio.src = URL.createObjectURL(blob);
            recordedAudio.controls = true;
            recordedAudio.autoplay = false;
        }
    }
}

function sendData(file, name, mode) {
    const XHR = new XMLHttpRequest();
    FD = new FormData()

    XHR.onreadystatechange = function () {
        if (XHR.readyState == XMLHttpRequest.DONE) {
            alert(XHR.responseText);
        }
    }

    FD.append("username", name);
    FD.append('audio', file, 'audio');

    if (mode == 'enroll') {
        XHR.open('POST', "http://127.0.0.1:8000/enroll", true);
    } else {
        XHR.open('POST', "http://127.0.0.1:8000/verify", true);
    }

    XHR.send(FD);
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

enroll.onclick = e => {
    console.log('Enroll pressed.')
    let name = prompt("Enter the profile name to be enrolled").toLowerCase();
    sendData(blob, name, 'enroll');
}

verify.onclick = e => {
    console.log('Verify pressed')
    let name = prompt("Enter the profile name to be verified").toLowerCase();
    sendData(blob, name, 'verify');
}

clear.onclick = e => {
    const XHR = new XMLHttpRequest();
    XHR.onreadystatechange = function () {
        if (XHR.readyState == XMLHttpRequest.DONE) {
            alert(XHR.responseText);
        }
    }
    XHR.open('GET', "http://127.0.0.1:8000/clear", true);
    XHR.send();
}