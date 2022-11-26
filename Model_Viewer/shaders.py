vertex_shader = """
#version 460
layout (location=0) in vec3 vertexPos;
layout (location=1) in vec2 vertexTexCoord;

uniform mat4 model;
uniform mat4 projection;

out vec2 fragmentTexCoord;

void main()
{
    gl_Position = projection * model * vec4(vertexPos, 1.0);
    fragmentTexCoord = vertexTexCoord;
}
"""

fragment_shader = """
#version 460
in vec2 fragmentTexCoord;

uniform sampler2D imageTexture;
uniform vec3 colorRandom;
uniform int op;
uniform float u_time;

out vec4 color;

void main()
{

    vec4 colorM = vec4(0.0);
    vec4 colorA = vec4(0.149, 0.141, 0.912, 1.0);
    vec4 colorB = vec4(colorRandom.xyz, 1.0);

    float pct = abs(sin(u_time));

    colorM = mix(colorA, colorB, pct);
    
    if (op == 1){
        color = texture(imageTexture, fragmentTexCoord) * vec4(colorRandom.xyz, 1.0);
    }
    else{
        color = texture(imageTexture, fragmentTexCoord) * vec4(colorM.xyz-colorRandom.xyz+0.3, 1.0);
    }
}
"""