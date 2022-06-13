#version 330 core

in vec3 newColor;

out vec4 outColor;
uniform sampler2D texSampler;

void main()
{
    outColor = vec4(newColor, 1.0);
}
