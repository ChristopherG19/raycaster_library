# Universidad del Valle de Guatemala
# Gráficas por computadora
# Christopher García 20541
# Raycaster

import random
import pyrr
import pygame
import glm
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram,compileShader
from shaders import *
from material import *
from utilities import *

class App:
    def __init__(self):
        pygame.init()
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        pygame.display.set_mode((850,650), pygame.OPENGL|pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()

        glClearColor(0.1, 0.2, 0.2, 1)
        self.cube_mesh = Mesh("Cube.obj")
        self.shader = self.createShader(vertex_shader, fragment_shader)
        glUseProgram(self.shader)
        
        color1 = random.random()
        color2 = random.random()
        color3 = random.random()
        
        color = glm.vec3(color1, color2, color3)
        
        glUniform3fv(
            glGetUniformLocation(self.shader, 'colorRandom'),
            1, 
            glm.value_ptr(color)
        )
        
        glUniform1i(glGetUniformLocation(self.shader, 'op'), 1)
        glUniform1f(glGetUniformLocation(self.shader, 'u_time'), 0.6)
        
        glUniform1i(glGetUniformLocation(self.shader, "imageTexture"), 0)
        glEnable(GL_DEPTH_TEST)
        
        self.texture = Material("Concrete.jpg")

        self.cube = Cube(
            position = [0,0,-6],
            eulers = [0,0,0]
        )

        projection_transform = pyrr.matrix44.create_perspective_projection(
            fovy = 45, aspect = 640/480, 
            near = 0.1, far = 10, dtype=np.float32
        )
        glUniformMatrix4fv(
            glGetUniformLocation(self.shader,"projection"),
            1, GL_FALSE, projection_transform
        )
        
        self.modelMatrixLocation = glGetUniformLocation(self.shader,"model")
        self.mainLoop()

    def createShader(self, vertexFilepath, fragmentFilepath):

        shader = compileProgram(
            compileShader(vertexFilepath, GL_VERTEX_SHADER),
            compileShader(fragmentFilepath, GL_FRAGMENT_SHADER)
        )
        
        return shader

    def mainLoop(self):
        running = True
        while (running):
            op = 1
            keys = pygame.key.get_pressed()
            
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_ESCAPE):
                        running = False
        
            # Zoom in          
            if keys[K_q]:
                self.cube.position[2] += 0.15
                if self.cube.position[2] > -1.8:
                    self.cube.position[2] -= 0.15
        
            # Zoom out        
            elif keys[K_e]:
                self.cube.position[2] -= 0.15
                if self.cube.position[2] < -9:
                    self.cube.position[2] += 0.15
                    
            elif keys[K_a]:
                self.cube.position[0] += 0.1
                if self.cube.position[0] > 1.6:
                    self.cube.position[0] -= 0.1
             
            elif keys[K_d]:
                self.cube.position[0] -= 0.1
                if self.cube.position[0] < -1.6:
                    self.cube.position[0] += 0.1
            
            elif keys[K_s]:
                self.cube.position[1] += 0.1
                if self.cube.position[1] > 1.05:
                    self.cube.position[1] -= 0.1
                    
            elif keys[K_w]:
                self.cube.position[1] -= 0.1
                if self.cube.position[1] < -1.05:
                    self.cube.position[1] += 0.1
            
            elif keys[K_c]:
                color1 = random.random()
                color2 = random.random()
                color3 = random.random()
                
                color = glm.vec3(color1, color2, color3)
                glUniform1i(glGetUniformLocation(self.shader, 'op'), 1)
                glUniform3fv(
                    glGetUniformLocation(self.shader, 'colorRandom'),
                    1, 
                    glm.value_ptr(color)
                )
            
            elif keys[K_v]:
                
                op = random.randint(2, 5)
                
                for i in range(0 ,5):
                    u_time = 0.2 * i
                    glUniform1i(glGetUniformLocation(self.shader, 'op'), op)
                    glUniform1f(glGetUniformLocation(self.shader, 'u_time'), u_time)
            
            # Reset                
            elif keys[K_r]:
                self.cube.position = [0,0,-6]
                self.cube.eulers = [0,0,0]
            
            # Rotate Left
            if keys[K_LEFT]:
                self.cube.eulers[2] += 0.35
                if self.cube.eulers[2] > 360:
                    self.cube.eulers[2] -= 360
                    
            # Rotate Right        
            elif keys[K_RIGHT]:
                self.cube.eulers[2] -= 0.35
                if self.cube.eulers[2] < 1:
                    self.cube.eulers[2] += 360
                    
            # Rotate Up
            elif keys[K_UP]:
                self.cube.eulers[0] += 0.35
                if self.cube.eulers[0] > 360:
                    self.cube.eulers[0] -= 360
            
            # Rotate Down
            elif keys[K_DOWN]:
                self.cube.eulers[0] -= 0.35
                if self.cube.eulers[0] < 1:
                    self.cube.eulers[0] += 360 
            
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glUseProgram(self.shader)

            model_transform = pyrr.matrix44.create_identity(dtype=np.float32)

            model_transform = pyrr.matrix44.multiply(
                m1=model_transform, 
                m2=pyrr.matrix44.create_from_eulers(
                    eulers=np.radians(self.cube.eulers), 
                    dtype=np.float32
                )
            )
            model_transform = pyrr.matrix44.multiply(
                m1=model_transform, 
                m2=pyrr.matrix44.create_from_translation(
                    vec=np.array(self.cube.position),
                    dtype=np.float32
                )
            )
            glUniformMatrix4fv(self.modelMatrixLocation,1,GL_FALSE,model_transform)
            self.texture.use()
            glBindVertexArray(self.cube_mesh.vao)
                
            glDrawArrays(GL_TRIANGLES, 0, self.cube_mesh.vertex_count)

            pygame.display.flip()

            self.clock.tick(60)
        self.quit()

    def quit(self):
        self.cube_mesh.destroy()
        self.texture.destroy()
        glDeleteProgram(self.shader)
        pygame.quit()

myApp = App()