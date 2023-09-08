import './style.css'
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';
import { VRButton } from 'three/examples/jsm/webxr/VRButton.js';


const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);

const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });

//const controls = new OrbitControls(camera, renderer.domElement);

renderer.xr.enabled = true;
renderer.setPixelRatio(window.devicePixelRatio);
renderer.setClearColor(0x000000);
renderer.setSize(window.innerWidth, window.innerHeight);
camera.position.set(5, 0, 0);

// const groundGeometry = new THREE.PlaneGeometry( 20, 20, 32, 32 );
// groundGeometry.rotateX( - Math.PI / 2 );
// const groundMaterial = new THREE.MeshBasicMaterial( {
//     color: 0x555555, 
//     side: THREE.DoubleSide
// });
// const groundMesh = new THREE.Mesh( groundGeometry, groundMaterial );
// scene.add( groundMesh );

// Define your render function
function render() {
    model.rotation.y += 0.01;
    renderer.render(scene, camera);
}

// Set the animation loop
renderer.setAnimationLoop(render);

const pointLight1 = new THREE.PointLight(0xffffff, 10);
pointLight1.position.set(-5, 5, -5);

const pointLight2 = new THREE.PointLight(0xffffff, 10);
pointLight2.position.set(5, 5, -5);

const pointLight3 = new THREE.PointLight(0xffffff, 10);
pointLight3.position.set(-5, 5, 5);

const pointLight4 = new THREE.PointLight(0xffffff, 10);
pointLight4.position.set(5, 5, 5);

scene.add(pointLight1);
scene.add(pointLight2);
scene.add(pointLight3);
scene.add(pointLight4);


const lightHelper1 = new THREE.PointLightHelper(pointLight1)
const lightHelper2 = new THREE.PointLightHelper(pointLight2)
const lightHelper3 = new THREE.PointLightHelper(pointLight3)
const lightHelper4 = new THREE.PointLightHelper(pointLight4)
scene.add(lightHelper1);
scene.add(lightHelper2);
scene.add(lightHelper3);
scene.add(lightHelper4);

// const spotlight = new THREE.SpotLight(0xffffff, 10 , 10, 0.6, 0.5);
// spotlight.position.set(0, 10, 0);
// scene.add(spotlight);
// const spotlightHelper = new THREE.SpotLightHelper(spotlight)
// scene.add(spotlightHelper);

const loader = new GLTFLoader();

let model;

loader.load('./models/wooden_chess_set.glb', function ( gltf ) {

	gltf.scene.scale.set(25,25,25);
    scene.add( gltf.scene );
    model = gltf.scene;
    

},function ( xhr ) {

    console.log( ( xhr.loaded / xhr.total * 100 ) + '% loaded' );

}, undefined, function ( error ) {

	console.error( error );

} );



const ambientLight = new THREE.AmbientLight(0xffffff);
scene.add(ambientLight);

document.body.appendChild(VRButton.createButton(renderer));

const dolly = new THREE.Object3D();
dolly.position.set(0, 5, 5);
dolly.add(camera);
scene.add(dolly);

const objec = new THREE.Object3D();
objec.position.set(0, 0, 0);
objec.add(model);

scene.add(objec);
