//--------------------
      // GET USER MEDIA CODE
      //--------------------
      var r=1;
          navigator.getUserMedia = ( navigator.getUserMedia ||
                             navigator.webkitGetUserMedia ||
                             navigator.mozGetUserMedia ||
                             navigator.msGetUserMedia);

      var video;
      var webcamStream;

      function startWebcam() {
        if (navigator.getUserMedia) {
           navigator.getUserMedia (

              // constraints
              {
                 video: true,
                 audio: false
              },

              // successCallback
              function(localMediaStream) {
                  video = document.querySelector('video');

                  /*video.srcObject=stream;
                  video.play();

                 video.src = window.URL.createObjectURL(localMediaStream);
                 webcamStream = localMediaStream;*/
                 video.srcObject=localMediaStream;
                  video.play();
              },

              // errorCallback
              function(err) {
                 console.log("The following error occured: " + err);
              }
           );
        } else {
           console.log("getUserMedia not supported");
        }  
      }

      function stopWebcam() {
          var track = stream.getTracks()[0];  // if only one media track
// ...
          track.stop();
      }
      //---------------------
      // TAKE A SNAPSHOT CODE
      //---------------------
      var canvas, ctx;

      function init() {
        // Get the canvas and obtain a context for
        // drawing in it
        //startWebcam();
        canvas = document.getElementById("myCanvas");
        ctx = canvas.getContext('2d');
        startWebcam();
      }

      function snapshot() {
         // Draws current image from the video element into the canvas
        ctx.drawImage(video, 0,0, canvas.width, canvas.height);
        return new Promise((res, rej)=>{
          canvas.toBlob(res, 'image/jpeg'); // request a Blob from the canvas
        });
      }
      function download(blob){
  // uses the <a download> to download a Blob
  let a = document.createElement('a'); 
  a.href = URL.createObjectURL(blob);
  a.download = r+'.jpg';
  r++;
  document.body.appendChild(a);
  a.click();
}