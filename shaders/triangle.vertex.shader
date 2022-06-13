#version 330 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoord;
layout (location = 2) in vec3 a_normal;


out vec2 outTextCoord;
uniform mat4 model;
uniform mat4 projection;
uniform mat4 view;

void main()
{
    gl_Position = projection * view * model * vec4(position.x, position.y, position.z, 1);
	// outTextCoord = texCoord
	outTextCoord = vec2(texCoord.x, 1.0 - texCoord.y);
	
}
