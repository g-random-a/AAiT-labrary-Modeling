#version 330

in vec3 position;
in vec3 color;
out vec3 newColor;


void main() {

  gl_Position = position;
  newColor = color;
      }