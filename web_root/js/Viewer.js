
class Viewer {

    constructor() {

        // Setup Camera
        this.width = 800;
        this.height = 600;
        this.scene = new THREE.Scene();
        this.camera = new THREE.PerspectiveCamera(75, this.width / this.height, 0.1, 1000);
        this.camera.position.z = 50;
        
        // Setup renderer
        this.renderer = new THREE.WebGLRenderer();
        this.renderer.setSize(this.width, this.height);
        this.renderer.setClearColor( 0x404040, 1);
        this.controls = new THREE.OrbitControls(this.camera, this.renderer.domElement);
        
        // Attach to dom
        this.container = document.getElementById('3d-container');
        this.container.appendChild(this.renderer.domElement)
        
        const directionalLight = new THREE.DirectionalLight(0xA1A1A1, 1);
        directionalLight.position.set(10, 100, 0);
        directionalLight.target.position.set(0, 0, 0);
        this.scene.add(directionalLight);
        this.scene.add(directionalLight.target);
        console.log('Viewer initialized.');
    }

    updatePoints(points) {
        var pointsObject = this.scene.getObjectByName('points');
        this.scene.remove(pointsObject);

        const vertices = [];
        const colors = [];
        
        for (let i=0; i < points.x.length; i++) {
            vertices.push(points.x[i], points.y[i], points.z[i]);
            colors.push(points.r[i], points.g[i], points.b[i]);
        }

        const geometry = new THREE.BufferGeometry();
        geometry.setAttribute('position', new THREE.Float32BufferAttribute(vertices, 3));
        geometry.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));

        const material = new THREE.PointsMaterial({size: 1, vertexColors: true});

        this.points = new THREE.Points(geometry, material);
        this.points.name = 'points';
        this.scene.add(this.points);
    }
    animate(timestamp) {
        requestAnimationFrame(() => {this.animate(timestamp)});
        this.controls.update();
        this.renderer.render(this.scene, this.camera);
    }
}
