/* global $ */
'use strict';

var recordingBlob;
window.recorderURL = undefined;
var video = document.getElementById('video');
var recording = false;

var startRecording = $('#start-recording');
var submitRecording = $('#submit-recording');

startRecording.click(function() {
    if (!recording) {
      recording = true;
      startRecording.text('Stop Recording');
      submitRecording.prop('disabled', true);
      captureUserMedia(function(stream) {
          window.audioVideoRecorder = window.RecordRTC(stream);
          window.audioVideoRecorder.startRecording();
      });
    } else {
      recording = false;
      startRecording.text('Start Recording');
      window.audioVideoRecorder.stopRecording(function(url) {
        submitRecording.prop('disabled', false);
        recordingBlob = url;
        video.src = url;
      });
    }
});

function captureUserMedia(callback) {
    navigator.getUserMedia = navigator.mozGetUserMedia || navigator.webkitGetUserMedia;
    navigator.getUserMedia({ audio: true, video: true }, function(stream) {
        video.src = URL.createObjectURL(stream);
        callback(stream);
    }, function(error) { console.error(error); });
}

submitRecording.click(function(){
  var xhr = new XMLHttpRequest();
  xhr.open('GET', recordingBlob, true);
  xhr.responseType = 'blob';
  xhr.onload = function(e) {
    console.log('onload', this, e);
    var myBlob = this.response;
    var formData = new FormData();
    formData.append('file', myBlob, 'file.webm');
    var oReq = new XMLHttpRequest();
    oReq.open('POST', window.recorderURL, true);
    oReq.onload = function (oEvent) {
      document.location.href = document.location.href;
    };
    oReq.send(formData);
  };
  xhr.send();
});

var setRecorder = function(url) {
  window.recorderURL = url;
};