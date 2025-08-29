// Three.js Scene Setup
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById("three-canvas"), alpha: true });

renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Load Baby Model
const loader = new THREE.GLTFLoader();
let babyModel;
loader.load('/static/baby.glb', (gltf) => {
    babyModel = gltf.scene;
    babyModel.position.set(0, -1, -3);
    scene.add(babyModel);
});

// Floating Toys with Dynamic Colors
function getRandomPastelColor() {
    const hue = Math.floor(Math.random() * 360);
    return `hsl(${hue}, 80%, 85%)`;
}

const toyGeometry = new THREE.SphereGeometry(0.3, 32, 32);
const toyMaterial1 = new THREE.MeshBasicMaterial({ color: getRandomPastelColor() });
const toyMaterial2 = new THREE.MeshBasicMaterial({ color: getRandomPastelColor() });

const toy1 = new THREE.Mesh(toyGeometry, toyMaterial1);
const toy2 = new THREE.Mesh(toyGeometry, toyMaterial2);

toy1.position.set(-2, 1, -2);
toy2.position.set(2, 2, -2);
toy1.classList.add("floating-toy");
toy2.classList.add("floating-toy");

scene.add(toy1, toy2);

// Animation Loop
function animate() {
    requestAnimationFrame(animate);
    toy1.position.y = Math.sin(Date.now() * 0.001) * 1 + 1;
    toy2.position.y = Math.cos(Date.now() * 0.001) * 1 + 1;
    renderer.render(scene, camera);
}

animate();
