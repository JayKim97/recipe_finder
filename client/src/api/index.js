import axios from 'axios';
const API = axios.create({baseURL: "http://localhost:5000"})

API.interceptors.request.use((req)=>{
  if(localStorage.getItem("profile")){
    req.headers.Authorization = `Bearer ${
      JSON.parse(localStorage.getItem("profile")).token
    }`
  }
  return req;
})


export const signup = (formData) => API.post("/user/signup", formData);
export const signin = (formData) => API.post("/user/login", formData);

export const getRecipes = () => API.get("/recipes");
export const createRecipe = (formData) => API.post("/recipes",formData);
export const getRecipe = (id) => API.get(`/recipes/${id}`);
export const editRecipe = (id,updatedRecipe) => API.patch(`/recipes/${id}`,updatedRecipe);
export const likeRecipe = (id) => API.patch(`/recipes/${id}/like`);
export const dislikeRecipe = (id) => API.patch(`/recipes/${id}/dislike`);
export const saveRecipe = (id) => API.patch(`/recipes/${id}/save`);
export const deleteRecipe = (id) => API.delete(`/recipes/${id}`);

export const getUserLiked = () => API.get('/user/liked');
export const getUserSaved = () => API.get('/user/saved');